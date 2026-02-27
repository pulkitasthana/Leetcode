class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        
        if z == 0:
            return 0
        
        if k == n:
            if z == n:
                return 1
            return -1
        
        for t in range(1, n + 1):
            total = t * k
            
            if total < z:
                continue
            
            if (total - z) % 2 != 0:
                continue
            
            # compute max possible total flips with parity constraint
            if t % 2 == 0:
                max_odd = t - 1
                max_even = t
            else:
                max_odd = t
                max_even = t - 1
            
            max_total = z * max_odd + (n - z) * max_even
            
            if total <= max_total:
                return t
        
        return -1