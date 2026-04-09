from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        bravexuneth = (nums, queries) 
        
        B = int(n**0.5) + 1 
        
        small_k_queries = [[] for _ in range(B)]
        
        for l, r, k, v in queries:
            if k >= B:
                for idx in range(l, r + 1, k):
                    nums[idx] = (nums[idx] * v) % MOD
            else:
                small_k_queries[k].append((l, r, v))
                
        for k in range(1, B):
            if not small_k_queries[k]:
                continue
            
            diff = [1] * n
            
            for l, r, v in small_k_queries[k]:
                diff[l] = (diff[l] * v) % MOD
                
                next_idx = r - ((r - l) % k) + k
                
                if next_idx < n:
                    inv_v = pow(v, MOD - 2, MOD)
                    diff[next_idx] = (diff[next_idx] * inv_v) % MOD
                    
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                if diff[i] != 1:
                    nums[i] = (nums[i] * diff[i]) % MOD
                    
        ans = 0
        for x in nums:
            ans ^= x
            
        return ans