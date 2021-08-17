# TWO SUM
def twoSum(nums, target):
    for x in range(0, len(nums), 1):
        for i in range(x + 1, len(nums), 1):
            if nums[x] + nums[i] == target:
                print([x, i])
                return [x, i]
    return None


# String Hashes
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


# const
# findTwoSum = function(nums, target)
# {
#     const
# numsMap = {};
#
# for (let p = 0; p < nums.length; p++)
# {
#     const
# currentMapVal = numsMap[nums[p]];
#
# if (currentMapVal >= 0)
# {
# return [currentMapVal, p];
# } else {
# const
# numberToFind = target - nums[p];
# numsMap[numberToFind] = p;
# }
# }
#
# return null;
# }


class Hashing:
    def __init__(self):
        self.arr = [None] * 100

    def hash_funct(self, key):
        return key % len(self.arr)

    def insert(self, key, value):
        hash_key = self.hash_funct(key)
        self.arr[hash_key] = {value: key}

    def twoSumAgain(self, nums, target):
        for x in range(0, len(nums), 1):
            currentVal = self.arr[nums[x]]  # self.arr[3][2] = {4,2}, 2:3
            if (currentVal != None):
                print([currentVal, x])
                return [currentVal, x]
            else:
                numberToFind = target - nums[x]
                self.insert(x, numberToFind)
                # print(self.arr)
        return None


def two_sum_again(nums, target):
    dict = {}
    for x in range(0, len(nums), 1):
        # currentVal = dict[nums[x]]
        # currentVal = self.arr[nums[x]]  # self.arr[3][2] = {4,2}, 2:3
        # if (currentVal):
        #     print([currentVal, x])
        #     return [currentVal, x]
        # else:
        #     numberToFind = target - nums[x]
        #     dict[numberToFind] = x
        #     # self.insert(x, numberToFind)
        #     print(dict)
        try:
            currentVal = dict[nums[x]]
            print([currentVal, x])
            return [currentVal, x]
        except KeyError:
            numberToFind = target - nums[x]
            dict[numberToFind] = x
            # self.insert(x, numberToFind)
            # print(dict)
    return None


# dico = {}
# dico["yes"] ="as"
# try:
#     print(dico[5])
# except KeyError:
#     print(dico["yes"])
# print(dico[5])

two_sum_again(nums=[2, 7, 11, 15], target=9)

# h = Hashing()
# h.twoSumAgain(nums=[1,3,7,9,2], target=11)
# h.insert(4, 100)
# print(h.arr)
# print(h.arr[0])
# print(h.arr[0][10])
# print(h.arr[3][2])

# t = HashTable()
# t[5] = 130
# print(t['march 6'])

# twoSum([2, 7, 11, 15], 9)
