class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        product = 1   
        for i in range(len(nums)):
            answer.append(product)
            product = product*nums[i]       
        product = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i] = (answer[i]*product)
            product = product*nums[i]         
        return answer 
         