from typing import List
import bisect

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        pts = sorted(zip(robots, distance))
        robot_positions = [p[0] for p in pts]
        robot_set = set(robot_positions)
        
        walls.sort()
        wall_set = set(walls)
        at_robot_count = len(wall_set & robot_set)
        
        S = [w for w in walls if w not in robot_set]
        
        def count_in(low, high):
            if low > high:
                return 0
            return bisect.bisect_right(S, high) - bisect.bisect_left(S, low)
        
        r0, d0 = pts[0]
        r_next = pts[1][0] if n > 1 else float('inf')
        
        w0_l = count_in(r0 - d0, r0 - 1)
        w0_r = count_in(r0 + 1, min(r0 + d0, r_next))
        
        dp0 = w0_l
        dp1 = w0_r
        prev_w_r = w0_r
        
        for i in range(1, n):
            r_prev, d_prev = pts[i-1]
            r_curr, d_curr = pts[i]
            r_next = pts[i+1][0] if i + 1 < n else float('inf')
            
            w_l = count_in(max(r_prev, r_curr - d_curr), r_curr - 1)
            w_r = count_in(r_curr + 1, min(r_curr + d_curr, r_next))
            
            end_prev = min(r_curr, r_prev + d_prev)
            start_curr = max(r_prev, r_curr - d_curr)
            
            if end_prev < start_curr:
                w_union = count_in(r_prev + 1, end_prev) + count_in(start_curr, r_curr - 1)
            else:
                w_union = count_in(r_prev + 1, r_curr - 1)
            
            new_dp0 = max(dp0 + w_l, dp1 - prev_w_r + w_union)
            new_dp1 = max(dp0, dp1) + w_r
            
            dp0, dp1 = new_dp0, new_dp1
            prev_w_r = w_r
            
        return max(dp0, dp1) + at_robot_count