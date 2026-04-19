class Solution:
    def maxDistance(self, nums1, nums2):
        i, j = 0, 0
        max_dist = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1   # try to expand distance
            else:
                i += 1   # move i to reduce nums1[i]
        
        return max_dist