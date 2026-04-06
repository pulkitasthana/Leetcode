from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        # Convert obstacles list to set for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        # Directions: North, East, South, West
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0  # start facing North
        
        x, y = 0, 0
        max_dist = 0
        
        for cmd in commands:
            if cmd == -2:  # turn left
                d = (d + 3) % 4
            elif cmd == -1:  # turn right
                d = (d + 1) % 4
            else:
                dx, dy = dirs[d]
                
                for _ in range(cmd):  # move step by step
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist