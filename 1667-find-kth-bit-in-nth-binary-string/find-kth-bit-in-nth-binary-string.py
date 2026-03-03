class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def solve(n, k):
            if n == 1:
                return 0
            
            length = (1 << n) - 1
            mid = length // 2 + 1
            
            if k == mid:
                return 1
            elif k < mid:
                return solve(n - 1, k)
            else:
                mirrored = length - k + 1
                return 1 - solve(n - 1, mirrored)
        
        return str(solve(n, k))