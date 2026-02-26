class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        s = list(s)  # convert to list for easy modification
        
        while len(s) > 1:
            if s[-1] == '0':
                # even -> divide by 2
                s.pop()
            else:
                # odd -> add 1
                i = len(s) - 1
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1
                if i >= 0:
                    s[i] = '1'
                else:
                    s.insert(0, '1')
            steps += 1
        
        return steps