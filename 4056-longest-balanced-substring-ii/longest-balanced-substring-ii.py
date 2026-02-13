class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # Case 1: Substrings with 1 distinct character
        # We just need the longest run of identical characters.
        if n > 0:
            current_run = 1
            ans = 1
            for i in range(1, n):
                if s[i] == s[i-1]:
                    current_run += 1
                else:
                    current_run = 1
                ans = max(ans, current_run)
        
        # Case 2: Substrings with 2 distinct characters
        # Helper function to solve for pairs like (a, b) avoiding c
        def solve_two(c1, c2, forbidden):
            nonlocal ans
            # map stores {diff: first_index}
            # diff = count(c1) - count(c2)
            mapping = {0: -1}
            diff = 0
            
            for i, char in enumerate(s):
                if char == forbidden:
                    # Reset state, effectively treating the next index as a new start
                    mapping = {0: i}
                    diff = 0
                else:
                    if char == c1:
                        diff += 1
                    elif char == c2:
                        diff -= 1
                    
                    if diff in mapping:
                        ans = max(ans, i - mapping[diff])
                    else:
                        mapping[diff] = i

        solve_two('a', 'b', 'c')
        solve_two('a', 'c', 'b')
        solve_two('b', 'c', 'a')
        
        # Case 3: Substrings with 3 distinct characters
        # Condition: count(a) == count(b) == count(c)
        # We track the state (count_a - count_b, count_b - count_c)
        mapping = {(0, 0): -1}
        ca, cb, cc = 0, 0, 0
        
        for i, char in enumerate(s):
            if char == 'a': ca += 1
            elif char == 'b': cb += 1
            elif char == 'c': cc += 1
            
            # The state remains the same if the relative differences between counts are preserved
            key = (ca - cb, cb - cc)
            
            if key in mapping:
                ans = max(ans, i - mapping[key])
            else:
                mapping[key] = i
                
        return ans