class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        # build matrix row-wise
        matrix = []
        index = 0
        
        for i in range(rows):
            matrix.append(encodedText[index:index+cols])
            index += cols
        
        # read diagonally
        result = []
        
        for start_col in range(cols):
            r, c = 0, start_col
            
            while r < rows and c < cols:
                result.append(matrix[r][c])
                r += 1
                c += 1
        
        return "".join(result).rstrip()