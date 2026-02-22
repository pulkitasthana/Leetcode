class Solution:
    def binaryGap(self, n: int) -> int:
        last_pos = -1
        max_dist = 0
        position = 0
        
        while n > 0:
            if n & 1:   # if current bit is 1
                if last_pos != -1:
                    max_dist = max(max_dist, position - last_pos)
                last_pos = position
            
            n >>= 1
            position += 1
        
        return max_dist
        