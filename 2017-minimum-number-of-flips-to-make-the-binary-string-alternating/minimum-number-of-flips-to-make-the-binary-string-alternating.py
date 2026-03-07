class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        
        alt1 = ""
        alt2 = ""
        
        for i in range(len(s)):
            if i % 2 == 0:
                alt1 += '0'
                alt2 += '1'
            else:
                alt1 += '1'
                alt2 += '0'
        
        res = float('inf')
        diff1 = diff2 = 0
        left = 0
        
        for right in range(len(s)):
            
            if s[right] != alt1[right]:
                diff1 += 1
            if s[right] != alt2[right]:
                diff2 += 1
            
            if right - left + 1 > n:
                if s[left] != alt1[left]:
                    diff1 -= 1
                if s[left] != alt2[left]:
                    diff2 -= 1
                left += 1
            
            if right - left + 1 == n:
                res = min(res, diff1, diff2)
        
        return res   