class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        curr_char = ord('a')
        
        # Step 1: Greedily construct the lexicographically smallest string.
        # If lcp[i][j] > 0, word[i] must equal word[j].
        for i in range(n):
            if not word[i]:
                if curr_char > ord('z'):
                    return "" # More than 26 characters needed
                word[i] = chr(curr_char)
                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        word[j] = chr(curr_char)
                curr_char += 1
                
        # Step 2: Verify if the constructed string perfectly produces the given LCP matrix.
        # We process from bottom-right to top-left to dynamically check LCPs.
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    if i + 1 < n and j + 1 < n:
                        expected = 1 + lcp[i + 1][j + 1]
                    else:
                        expected = 1
                else:
                    expected = 0
                
                # If the actual LCP matrix doesn't match the expected rules, it's invalid.
                if lcp[i][j] != expected:
                    return ""
                    
        return "".join(word)