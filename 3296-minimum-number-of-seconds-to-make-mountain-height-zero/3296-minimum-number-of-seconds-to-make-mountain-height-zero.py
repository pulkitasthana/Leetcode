import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        
        def canFinish(T):
            total = 0
            for t in workerTimes:
                x = int((math.sqrt(1 + 8*T/t) - 1) // 2)
                total += x
                if total >= mountainHeight:
                    return True
            return False
        
        left = 0
        right = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if canFinish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans