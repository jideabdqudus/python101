# TWO SUM
def twoSum (nums, target):
    for x in range(0, len(nums), 1):
        for i in range(x+1, len(nums), 1):
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
        self.arr = [None] * 10

    def hash_funct(self, key):
        print(key % len(self.arr))
        return key % len(self.arr)

    def insert(self, key, value):
        hash_key = self.hash_funct(key)
        self.arr[hash_key] = value
        print(self.arr)


    def twoSumAgain (self, nums, target):
        for x in range(0, len(nums), 1):
            print(x)
            # currentVal = self.arr[nums[x]]
            # print(currentVal)
        return None



h = Hashing()
h.twoSumAgain(nums=[2, 7, 11, 15], target=9)
# h.insert(4, 100)
# print(h.arr[4])

# t = HashTable()
# t[5] = 130
# print(t['march 6'])

# twoSum([2, 7, 11, 15], 9)


















