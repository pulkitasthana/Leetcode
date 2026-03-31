class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        size = n + m - 1
        
        # Step 1: initialize result with '?'
        res = ['?'] * size
        
        # Step 2: enforce all 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i+j] == '?' or res[i+j] == str2[j]:
                        res[i+j] = str2[j]
                    else:
                        return ""
        
        # Step 3: fill remaining '?' with smallest letter
        for i in range(size):
            if res[i] == '?':
                res[i] = 'a'
        
        # Step 4: handle 'F' constraints
        for i in range(n):
            if str1[i] == 'F':
                if ''.join(res[i:i+m]) == str2:
                    
                    # try to break equality lexicographically minimally
                    changed = False
                    
                    for j in reversed(range(m)):
                        pos = i + j
                        
                        # try replacing with next smallest character
                        for c in range(ord('a'), ord('z')+1):
                            c = chr(c)
                            
                            if c != str2[j]:
                                
                                original = res[pos]
                                res[pos] = c
                                
                                # ensure we didn't break any 'T'
                                valid = True
                                for k in range(max(0, pos-m+1), min(pos+1, n)):
                                    if str1[k] == 'T':
                                        if ''.join(res[k:k+m]) != str2:
                                            valid = False
                                            break
                                
                                if valid:
                                    changed = True
                                    break
                                
                                res[pos] = original
                        
                        if changed:
                            break
                    
                    if not changed:
                        return ""
        
        return ''.join(res)