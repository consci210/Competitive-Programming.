class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge both sorted arrays
        merged = sorted(nums1 + nums2)
        length = len(merged)

    # Check if total length is even or odd
        if length % 2 == 1:
        # Odd length: return middle element
            return merged[length // 2]
        else:
        # Even length: average of two middle elements
            mid1 = merged[length // 2 - 1]
            mid2 = merged[length // 2]
            return (mid1 + mid2) / 2
            