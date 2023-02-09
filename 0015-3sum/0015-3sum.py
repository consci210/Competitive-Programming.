class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if (i == 0 or nums[i] != nums[i - 1]):
                target = nums[i] 
                left = i+1
                right = len(nums) - 1
                while left < right  :  
                    threeSum = nums[i] + nums[left] + nums[right]
                    if threeSum > 0:
                        right -= 1
                    elif threeSum < 0  :
                        left += 1
                    else :
                        answer.append([nums[i] , nums[left] , nums[right]])
                        left +=1 
                        while nums[left] == nums[left-1] and left<right :
                            left +=1    
        return answer 