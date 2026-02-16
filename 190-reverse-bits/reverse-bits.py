class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # 1. Shift result to the left to make room for the new bit
            result = result << 1
            
            # 2. Get the last bit of n
            bit = n & 1
            
            # 3. Add the bit to the least significant position of result
            result = result | bit
            
            # 4. Shift n to the right to process the next bit
            n = n >> 1
            
        return result
        