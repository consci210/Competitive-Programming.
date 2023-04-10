class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        greater = defaultdict(int)
        for i in range(len(nums)-1 , -1 , -1):
            for j in range(i+1 , len(nums)):
                if nums[j] > nums[i]:
                    if greater[nums[j]]+1 > greater[nums[i]] :
                        greater[nums[i]] = greater[nums[j]] + 1 
                        
           
        return max(greater.values())+ 1 if greater else 1