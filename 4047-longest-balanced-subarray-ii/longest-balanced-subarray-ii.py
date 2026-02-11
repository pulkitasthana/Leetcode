from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Parallel arrays for the segment tree to optimize speed and memory.
        # Size 4 * (n + 1) safely covers all nodes for the range [0, n].
        mn = [0] * ((n + 1) * 4)
        mx = [0] * ((n + 1) * 4)
        lazy = [0] * ((n + 1) * 4)
        
        def modify(u: int, cl: int, cr: int, l: int, r: int, v: int):
            if l <= cl and cr <= r:
                mn[u] += v
                mx[u] += v
                lazy[u] += v
                return
            
            # Inline pushdown
            lz = lazy[u]
            left = u * 2
            right = left + 1
            if lz != 0:
                mn[left] += lz
                mx[left] += lz
                lazy[left] += lz
                mn[right] += lz
                mx[right] += lz
                lazy[right] += lz
                lazy[u] = 0
                
            mid = (cl + cr) // 2
            if l <= mid:
                modify(left, cl, mid, l, r, v)
            if r > mid:
                modify(right, mid + 1, cr, l, r, v)
                
            # Inline pushup
            mn[u] = mn[left] if mn[left] < mn[right] else mn[right]
            mx[u] = mx[left] if mx[left] > mx[right] else mx[right]

        def query(u: int, cl: int, cr: int, target: int) -> int:
            if cl == cr:
                return cl
            
            # Inline pushdown
            lz = lazy[u]
            left = u * 2
            right = left + 1
            if lz != 0:
                mn[left] += lz
                mx[left] += lz
                lazy[left] += lz
                mn[right] += lz
                mx[right] += lz
                lazy[right] += lz
                lazy[u] = 0
                
            mid = (cl + cr) // 2
            
            # Binary search: Since the step size between adjacent elements is <= 1,
            # if the target is within the left child's min/max bounds, it MUST exist there.
            if mn[left] <= target <= mx[left]:
                return query(left, cl, mid, target)
            else:
                return query(right, mid + 1, cr, target)

        # nums[i] <= 10^5, so a flat array is faster than a hash map for tracking last occurrences.
        last = [0] * 100005 
        now = 0
        ans = 0
        
        for i in range(1, n + 1):
            x = nums[i - 1]
            det = 1 if (x & 1) == 0 else -1  # Even is +1, Odd is -1
            
            prev = last[x]
            if prev != 0:
                # Remove the old contribution of this element
                modify(1, 0, n, prev, n, -det)
            else:
                # If it's the first time seeing it, it permanently adds to our total distinct prefix sum
                now += det
                
            last[x] = i
            # Add the new contribution
            modify(1, 0, n, i, n, det)
            
            # Find the earliest index `j` where P[j] == now
            pos = query(1, 0, n, now)
            if i - pos > ans:
                ans = i - pos
                
        return ans