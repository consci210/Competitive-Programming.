class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        
        def backtrack(idx , arr) :
            if idx == len(nums) :
                answer.append(arr.copy())
                return 
            for i in range(idx , len(nums)):
                arr[i] , arr[idx] = arr[idx] , arr[i]
                backtrack(idx+1  , arr)
                arr[i] , arr[idx] = arr[idx] , arr[i]
        backtrack(0,nums)
        return answer 