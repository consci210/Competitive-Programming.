class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        first_half = {}
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                summ = nums1[i] + nums2[j] 
                first_half[summ] = first_half.get(summ ,0) + 1
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                summ = nums3[k]+nums4[l]
                complement = -1 * summ
                if complement in first_half :
                    count+=first_half[complement]
        return count 