class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        
        if n - k + 1 < (1 << k):
            return False
        
        seen = set()
        num = 0
        mask = (1 << k) - 1
        
        for i in range(n):
            num = ((num << 1) & mask) | int(s[i])
            
            if i >= k - 1:
                seen.add(num)
        
        return len(seen) == (1 << k)