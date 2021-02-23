class Solution:
    def twoSum(self, nums, target):
        lens = len(nums)
        for i in range(lens):
            for j in range(lens):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
