class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        list2 = list(nums.index(target) + i for i in range (nums.count(target)))
        return(list2)
