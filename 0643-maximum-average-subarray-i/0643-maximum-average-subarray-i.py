class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        maximum = current_sum 
        for i in range(k , len(nums)) :
            current_sum -= nums[i-k]
            current_sum += nums[i]
            if current_sum > maximum :
                maximum = current_sum
        return maximum / k
            
            
                