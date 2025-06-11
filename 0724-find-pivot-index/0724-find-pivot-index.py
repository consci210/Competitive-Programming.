class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixLeft = [0 for i in range(len(nums))]
        prefixRight = [0 for i in range(len(nums))]
        sumLeft = 0 
        sumRight = 0 
        for i in range(len(nums)):
            sumLeft+=nums[i]
            sumRight+=nums[len(nums)-1-i]
            prefixLeft[i]= sumLeft
            prefixRight[len(nums)-1-i] = sumRight
        print(prefixLeft, prefixRight)
        for i in range(len(nums)):
            if prefixLeft[i] == prefixRight[i]:
                return i 
        return -1 