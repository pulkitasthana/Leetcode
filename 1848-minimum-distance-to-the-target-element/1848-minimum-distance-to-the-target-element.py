class Solution:
    def getMinDistance(self, nums, target, start):
        return min(abs(i - start) for i, x in enumerate(nums) if x == target)