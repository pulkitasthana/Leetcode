from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        # Create a list of original indices
        indices = list(range(n))
        
        # Sort indices based on their corresponding starting positions
        indices.sort(key=lambda x: positions[x])
        
        stack = []
        
        for i in indices:
            if directions[i] == 'R':
                # Robot moves right, wait for potential collisions
                stack.append(i)
            else:
                # Robot moves left, process collisions with any 'R' robots in the stack
                while stack and healths[i] > 0:
                    top = stack[-1]
                    
                    if healths[i] > healths[top]:
                        # Left-moving robot survives, right-moving is destroyed
                        healths[i] -= 1
                        healths[top] = 0
                        stack.pop()
                    elif healths[i] < healths[top]:
                        # Right-moving robot survives, left-moving is destroyed
                        healths[top] -= 1
                        healths[i] = 0
                    else:
                        # Both are destroyed
                        healths[i] = 0
                        healths[top] = 0
                        stack.pop()
        
        # Return the remaining healths of the robots that survived
        return [h for h in healths if h > 0]