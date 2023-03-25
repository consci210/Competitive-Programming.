class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  
        answer = nums[0] + nums[1] + nums[len(nums)-1]
        
        for i in range(len(nums)-2) :
            
            left = i+1
            right = len(nums) - 1
            while left < right :
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < target :
                    left+=1
                elif current_sum > target :
                    right -=1
                else :
                    return current_sum 
                
                if abs(current_sum - target) < abs(answer - target):
                    answer = current_sum
                
        return answer
            
            