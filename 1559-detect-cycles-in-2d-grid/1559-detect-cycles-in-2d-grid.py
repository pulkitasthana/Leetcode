from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(x, y, px, py, char):
            visited[x][y] = True
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == char:
                    
                    # If not visited → continue DFS
                    if not visited[nx][ny]:
                        if dfs(nx, ny, x, y, char):
                            return True
                    
                    # If visited and not parent → cycle found
                    elif (nx, ny) != (px, py):
                        return True
            
            return False
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        
        return False
        