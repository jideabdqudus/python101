# const findTwoSum = (nums, target) => {
#     for (let i = 0; i<nums.length; i++) {
#         for (let j = i +1; j<nums.length; j++) {
#             if (nums[i] + nums[j] ===target)
#                 return [i,j]
#         }
#     }
#     return null;
# }

def twoSum(nums, target):
    print(target in nums)



twoSum([1, 3, 2, 7, 9], 9)