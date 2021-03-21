from django.http.response import JsonResponse
import json
import inspect
from accounts.decorators import user_is_authenticated
from accounts.views import getUserByAccessToken, getUserById
from apiutility.aws_s3bucket import upload_file
from apiutility.errorCodes import (ErrorCodes,
                                   getUnauthenticatedErrorPacket,
                                   getFormDoesNotExistErrorPacket)
from apiutility.jsonTransformer import (transformIndicatorList, transformProgram,
                                        transformProgramIndicatorTarget,
                                        transformProgramList, transformProgramSdg_and_Indicator_List,
                                        transformtotalbudgetandbeneficary)
from apiutility.models import Error
from apiutility.validators import (validateImage,
                                   validateKeys,
                                   validateThatListIsEmpty,
                                   validateThatStringIsEmpty,
                                   validateThatStringIsEmptyAndClean)
from apiutility.views import (badRequestResponse,
                              internalServerErrorResponse,
                              successResponse,
                              unAuthenticatedResponse,
                              resourceNotFoundResponse)
from core.views import (getIndicator, getSdgById)
from program.enums import IndicatorTypeEnum
from program.views import (createProgram as CreateProgramRecord,
                           createprogramIndicatorTarget as createprogramIndicatorTargetRecord,
                           getProgramByDetail, getProgramById, updateProgram as updatedProgramRecord,
                           getProgramIndicator, getProgramLocation,
                           getPrograms, createProgramSdg as createProgramSdgRecord, getprogramSdgs,
                           deleteprogram,
                           totalamount)


@user_is_authenticated
def programRouter(request):
    if request.method == 'POST':
        return createProgram(request)
    elif request.method == 'GET':
        return listPrograms(request)


@user_is_authenticated
def programSingleRouter(request, programId):
    if request.method == 'GET':
        return listProgramById(request, programId)
    elif request.method == 'POST':
        return updateProgram(request, programId)


@user_is_authenticated
def deleteProgramRouter(request, programId):
    if request.method == 'POST':
        return deleteProgram(request, programId)


@user_is_authenticated
def programIndicatorTargetRouter(request):
    if request.method == 'POST':
        return createprogramIndicatorTarget(request)
    elif request.method == 'GET':
        return ""


def totalRouter(request):
    if request.method == 'GET':
        return totalbudgetandbeneficary(request)


def createProgram(request):
    try:
        body = request.POST
        image = request.FILES['image'] if 'image' in request.FILES else False
        token = request.headers.get('accessToken')
        user = getUserByAccessToken(token)
        if image == False:
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message=f"please provide a valid image file")
        # check if all required fields are present in request payload
        missingKeys = validateKeys(payload=body,
                                   requiredKeys=['name', 'description', 'code', "locations", "sdgs", "budget",
                                                 "totalNumberOfBeneficiaries", "activeMarker"])
        if missingKeys:
            return badRequestResponse(errorCode=ErrorCodes.MISSING_FIELDS,
                                      message=f"The following key(s) are missing in the request payload: {missingKeys}")

        if not validateThatListIsEmpty(body['locations']):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message=f"Program must contain a list of locations")

        if not validateThatListIsEmpty(body['sdgs']):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message=f"Program must contain a list of sdgs and indicators")
        is_program_exist = getProgramByDetail(body['name'], body['description'], body['code'], user)
        if is_program_exist.exists():
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message=f"Program already exists")
        # validation for sdg
        for sdg in json.loads(body['sdgs']):
            missingSdgkey = validateKeys(payload=sdg, requiredKeys=['id', 'indicators'])
            if missingSdgkey:
                return badRequestResponse(ErrorCodes.MISSING_FIELDS,
                                          message=f"The following key(s) are missing in the request locations array payload: {missingSdgkey}")
            # check that sdg exist
            sdg_id = sdg['id']
            sdg_exist = getSdgById(sdg_id)
            if sdg_exist is None:
                return badRequestResponse(ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                          message=f"sgd {sdg_id} does not exist")
            # check that indicator exist
            sdg_indicators = sdg['indicators']
            for sdg_indicator in sdg_indicators:
                sdg_inidcator_exist = getIndicator(sdg_indicator)
                if sdg_inidcator_exist is None:
                    return badRequestResponse(ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                              message=f"selected sdg indicator {sdg_indicator} does not exist")

        token = request.headers.get('accessToken')
        user = getUserByAccessToken(token)
        if user is None:
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS, message=f"User does not exist")

        if not validateThatStringIsEmptyAndClean(body['name']):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message=f"Program name can neither contain special characters nor be empty")
        if not validateThatStringIsEmpty(body['description']):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message=f"Program description can neither contain special characters nor be empty",
                                      body={})
        if not validateThatStringIsEmptyAndClean(body['code']):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message=f"Program code can neither contain special characters nor be empty")
        if not validateThatStringIsEmptyAndClean(body['budget']):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message=f"budget can neither contain special characters nor be empty")
        if not validateThatStringIsEmptyAndClean(body['totalNumberOfBeneficiaries']):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message=f"Beneficiaries can neither contain special characters nor be empty")

        # load the fields from Json
        name = body['name']
        description = body['description']
        code = body['code']
        locations = json.loads(body['locations'])
        sdgs = json.loads(body['sdgs'])
        budget = body['budget']
        totalNumberOfBeneficiaries = body['totalNumberOfBeneficiaries']
        activeMarker = json.loads(body['activeMarker'])
        validate_image = validateImage(image.name)
        if validate_image is not None:
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS, message=validate_image)

        image_link = upload_file(image, image.name)

        program = CreateProgramRecord(name, image_link, description, code, locations, sdgs, user, budget,
                                      totalNumberOfBeneficiaries, activeMarker)
        programFormList = None

        if program is None:
            return internalServerErrorResponse(errorCode=ErrorCodes.PROGRAM_CREATION_FAILED,
                                               message=f"Program failed to create")
        else:
            return successResponse(message="successfully created program",
                                   body=transformProgram(program, program.location_set.all(),
                                                         program.program_sdg_set.all(), programFormList))

    except AttributeError as ex:
        return internalServerErrorResponse(errorCode=ErrorCodes.MISSING_FIELDS, message=f"missing attributes")
    except Exception as ex:
        # Log Exception
        return internalServerErrorResponse(errorCode=ErrorCodes.PROGRAM_CREATION_FAILED,
                                           message=f"program failed to create")


def updateProgram(request, programId):
    token = request.headers.get('accessToken')
    user = getUserByAccessToken(token)
    if user is None:
        return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS, message=f"User does not exist")
    programToUpdate = getProgramById(programId)
    if programToUpdate is None:
        return resourceNotFoundResponse(ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                        message="Program does not exist ")
    body = request.POST
    image = request.FILES['image'] if 'image' in request.FILES else False
    if image == False:
        return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                  message=f"please provide a valid image file")

    # check if all required fields are present in request payload
    missingKeys = validateKeys(payload=body, requiredKeys=['name', 'description', 'code', "locations", "sdgs", "budget",
                                                           "totalNumberOfBeneficiaries", "activeMarker"])
    if missingKeys:
        return badRequestResponse(errorCode=ErrorCodes.MISSING_FIELDS,
                                  message=f"The following key(s) are missing in the request payload: {missingKeys}")

    if not validateThatListIsEmpty(body['locations']):
        return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                  message=f"Program must contain a list of locations")
    if not validateThatListIsEmpty(body['sdgs']):
        return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                  message=f"Program must contain a list of sdgs and indicators")
    # validation for sdg
    for sdg in json.loads(body['sdgs']):
        missingSdgkey = validateKeys(payload=sdg, requiredKeys=['id', 'indicators'])
        if missingSdgkey:
            return badRequestResponse(ErrorCodes.MISSING_FIELDS,
                                      message=f"The following key(s) are missing in the request locations array payload: {missingSdgkey}")

        # check that sdg exist
        sdg_id = sdg['id']
        sdg_exist = getSdgById(sdg_id)
        if sdg_exist is None:
            return badRequestResponse(ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message=f"sgd {sdg_id} does not exist")
        # check that sdg indicator exist
        sdg_indicators = sdg['indicators']
        for sdg_indicator in sdg_indicators:
            sdg_inidcator_exist = getIndicator(sdg_indicator)
            if sdg_inidcator_exist is None:
                return badRequestResponse(ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                          message=f"selected sdg indicator {sdg_indicator} does not exist")
    if not validateThatStringIsEmptyAndClean(body['name']):
        return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                  message=f"Program name can neither contain special characters nor be empty")
    if not validateThatStringIsEmpty(body['description']):
        return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                  message=f"Program description can neither contain special characters nor be empty",
                                  body={})
    if not validateThatStringIsEmptyAndClean(body['code']):
        return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                  message=f"Program code can neither contain special characters nor be empty")
    if not validateThatStringIsEmptyAndClean(body['budget']):
        return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                  message=f"budget can neither contain special characters nor be empty")
    if not validateThatStringIsEmptyAndClean(body['totalNumberOfBeneficiaries']):
        return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                  message=f"Beneficiaries can neither contain special characters nor be empty")

    name = body['name']
    description = body['description']
    code = body['code']
    locations = json.loads(body['locations'])
    sdgs = json.loads(body['sdgs'])
    budget = body['budget']
    totalNumberOfBeneficiaries = body['totalNumberOfBeneficiaries']
    activeMarker = json.loads(body['activeMarker'])
    validate_image = validateImage(image.name)
    if validate_image is not None:
        return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS, message=validate_image)
    image_link = upload_file(image, image.name)
    updatedProgram = updatedProgramRecord(programToUpdate, name, description, image_link, code, locations, sdgs, user,
                                          budget, totalNumberOfBeneficiaries, activeMarker)
    if updatedProgram.form_program_set.all() is not None:
        updatedFormlist = updatedProgram.form_program_set.all()
    else:
        updatedFormlist = None
    # raise an error response if update wasn't successful
    if updatedProgram == None:
        return internalServerErrorResponse(ErrorCodes.PROGRAM_UPDATE_FAILED,
                                           message="Program update was unsuccessful")

    return successResponse(message="successfully updated program",
                           body=transformProgram(updatedProgram, updatedProgram.location_set.all(),
                                                 updatedProgram.program_sdg_set.all(), updatedFormlist))


def listPrograms(request):
    try:
        token = request.headers.get('accessToken')
        user = getUserByAccessToken(token)
        programs = getPrograms(user)
        return successResponse(message="programs fetched successfully", body=transformProgramList(programs))
    except Exception as ex:
        return internalServerErrorResponse(errorCode=ErrorCodes.GET_PROGRAM_LIST_FAILED,
                                           message="failed to fetch list of programs", data={})


def listProgramById(request, programId):
    try:
        program = getProgramById(programId)
        locations = getProgramLocation(program)
        if program.form_program_set.all() is not None:
            programFormlist = program.form_program_set.all()
        else:
            programFormlist = None
        if program is not None:
            return successResponse(message="program fetched successfully",
                                   body=transformProgram(program, locations, program.program_sdg_set.all(),
                                                         programFormlist))
        else:
            return successResponse(message="program does not exist", body={})
    except Exception as ex:
        # Log Error
        return internalServerErrorResponse(errorCode=ErrorCodes.GET_PROGRAM_SINGLE_FAILED,
                                           message=f"failed to fetch program id = {programId}")


def createprogramIndicatorTarget(request):
    try:
        body = json.loads(request.body)
        missingKeys = validateKeys(payload=body, requiredKeys=[
            'programIndicatorId', 'name', 'type', 'value'])
        if missingKeys:
            return badRequestResponse(ErrorCodes.MISSING_FIELDS,
                                      message=f"The following key(s) are missing in the request payload: {missingKeys}")
        type = body['type']
        value = body['value']
        programIndicatorId = body['programIndicatorId']
        name = body['name']
        if not validateThatStringIsEmpty(type):
            return badRequestResponse(errorCode=ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message="type can neither contain special characters nor be empty")
            # Validate the type as 'numeric' or 'percentage'
        if not IndicatorTypeEnum.has_value(type):
            return badRequestResponse(ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                      message="please indicate type as 'number' or 'percentage' ")
        # check value if type is percentage
        if type == IndicatorTypeEnum.PERCENTAGE.value:
            if value < 0 or value > 100:
                return badRequestResponse(ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                          message="The value of a percentage based indicator cannot be less than 0 or more than 100")
        else:
            if value < 0:
                return badRequestResponse(ErrorCodes.GENERIC_INVALID_PARAMETERS,
                                          message="The value of a number based indicator cannot be less than 0")

        programIndicator = getProgramIndicator(programIndicatorId)
        # Validate Indicator Field
        if programIndicator is None:
            return badRequestResponse(ErrorCodes.PROGRAM_INDICATOR_DOES_NOT_EXIST,
                                      message="please provide a valid program indicatorId")

        program_indicator_target = createprogramIndicatorTargetRecord(programIndicator, name, type, value)
        if program_indicator_target is None:
            return internalServerErrorResponse(errorCode=ErrorCodes.PROGRAM_INDICATOR_TARGET_CREATION_FAILED,
                                               message="Failed to create program indicator target")
        else:
            return successResponse(message="successfully created your target",
                                   body=transformProgramIndicatorTarget(program_indicator_target))
    except Exception as ex:
        pass


def deleteProgram(request, programId):
    token = request.headers.get('accessToken')
    user = getUserByAccessToken(token)
    if user is None:
        return unAuthenticatedResponse(ErrorCodes.UNAUTHENTICATED_REQUEST,
                                       message=getUnauthenticatedErrorPacket(userId=0))
    # Getting the program to be deleted
    programToDelete = getProgramById(programId)
    # deleting program from the database
    if programToDelete != None:
        status, deletedform = deleteprogram(programToDelete)
        if status is False:
            return internalServerErrorResponse(ErrorCodes.FORM_DELETION_FAILED,
                                               message="Something Went Wrong, Couldn't Delete Program")
        # return success
        return successResponse(message="Successfully deleted Form", body={})
    return resourceNotFoundResponse(ErrorCodes.PROGRAM_DOES_NOT_EXIST,
                                    message=getFormDoesNotExistErrorPacket(userId=user.id))


def totalbudgetandbeneficary(request):
    token = request.headers.get('accessToken')
    user = getUserByAccessToken(token)
    if user is None:
        return unAuthenticatedResponse(ErrorCodes.UNAUTHENTICATED_REQUEST,
                                       message=getUnauthenticatedErrorPacket(userId=0))
    userId = user.id
    totalbudget, totalbeneficaries = totalamount(userId)
    if totalamount and totalbeneficaries is None:
        return resourceNotFoundResponse(ErrorCodes.PROGRAM_DOES_NOT_EXIST,
                                        message=getFormDoesNotExistErrorPacket(userId=user.id))
    return successResponse(message="Total budget and beneficaries",
                           body=transformtotalbudgetandbeneficary(totalbudget, totalbeneficaries))