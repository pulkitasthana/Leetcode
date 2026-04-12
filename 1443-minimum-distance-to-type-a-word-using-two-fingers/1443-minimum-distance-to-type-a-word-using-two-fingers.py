class Solution:
    def minimumDistance(self, word: str) -> int:
        
        def dist(a, b):
            if a == -1: return 0
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(word)
        dp = [0] * 26  # max saving
        total = 0
        
        for i in range(1, n):
            cur = ord(word[i]) - ord('A')
            prev = ord(word[i-1]) - ord('A')
            
            d = dist(prev, cur)
            total += d
            
            new_dp = dp[:]
            
            for b in range(26):
                # move second finger from b → cur
                gain = dp[b] + d - dist(b, cur)
                new_dp[prev] = max(new_dp[prev], gain)
            
            dp = new_dp
        
        return total - max(dp)