class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        reversed_n = 0
        
        while n > 0:
            digit = n % 10
            reversed_n = reversed_n * 10 + digit
            n //= 10
        
        return abs(original - reversed_n)