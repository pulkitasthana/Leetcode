class Solution:
    
    def rotate(self, mat):
        n = len(mat)
        rotated = [[0]*n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                rotated[i][j] = mat[n-j-1][i]
        
        return rotated
    
    
    def findRotation(self, mat, target):
        
        for _ in range(4):
            if mat == target:
                return True
            
            mat = self.rotate(mat)
        
        return False