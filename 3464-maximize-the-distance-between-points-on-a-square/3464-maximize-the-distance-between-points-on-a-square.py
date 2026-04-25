from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # 1. Linearize the points along the perimeter
        linear_points = []
        for x, y in points:
            if y == 0:          # Bottom edge
                d = x
            elif x == side:     # Right edge
                d = side + y
            elif y == side:     # Top edge
                d = 2 * side + (side - x)
            else:               # Left edge (x == 0)
                d = 3 * side + (side - y)
            linear_points.append((d, x, y))
        
        linear_points.sort()
        n = len(linear_points)
        perimeter = 4 * side
        
        def get_manhattan(p1, p2):
            return abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

        def can_place(min_dist):
            # Since it's a circle, the first point chosen matters.
            # We only need to try starting from points that could be in the first 'gap'
            # To be safe and efficient, we can try starting within the first points
            # but usually, checking starts from the first few points is enough.
            for i in range(n):
                # Optimization: if the distance from start to end of array 
                # doesn't allow k points, we can't just check i=0.
                # However, for k <= 25, we can afford a bit more.
                if i > 0 and linear_points[i][0] - linear_points[0][0] >= min_dist:
                    break
                
                count = 1
                last_idx = i
                first_point = linear_points[i]
                
                curr = i
                for _ in range(k - 1):
                    # Find next point at least min_dist away (Manhattan)
                    next_idx = -1
                    low = curr + 1
                    high = n + i - 1 # Search in the "circular" extended array
                    
                    found = False
                    # Simple linear scan is fine for k=25, or use binary search
                    p_idx = curr + 1
                    while p_idx < n + i:
                        actual_idx = p_idx % n
                        if get_manhattan(linear_points[last_idx], linear_points[actual_idx]) >= min_dist:
                            # Also must check distance to the very first point to close the loop
                            if p_idx < n + i: 
                                last_idx = actual_idx
                                curr = p_idx
                                count += 1
                                found = True
                                break
                        p_idx += 1
                    if not found: break
                
                if count == k:
                    # Final check: distance between last point and first point
                    if get_manhattan(linear_points[last_idx], first_point) >= min_dist:
                        return True
            return False

        # 2. Binary search for the maximum minimum distance
        ans = 0
        low = 1
        high = 2 * side # Max possible Manhattan distance is opposite corners
        
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans