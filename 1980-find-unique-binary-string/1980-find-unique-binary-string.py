from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        # Construct a string by flipping the i-th bit of nums[i]
        result = []
        for i in range(n):
            result.append('1' if nums[i][i] == '0' else '0')
        return "".join(result)
