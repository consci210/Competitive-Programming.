class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = [-1]*len(nums1)
        for i in range(len(nums1)):
            target = nums1[i]
            targetIndex = nums2.index(target)
            for j in range(targetIndex , len(nums2)):
                if nums2[j] > target :
                    answer[i] = nums2[j]
                    break 
        return answer 
            