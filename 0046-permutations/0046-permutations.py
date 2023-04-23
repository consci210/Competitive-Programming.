class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        def permutations(arr=[], used={}):
            if len(arr) == len(nums) :
                answer.append(arr.copy())
                return 
            for i in range(len(nums)):
                if i not in used :
                    used[i] = 1 
                    arr.append(nums[i])
                    permutations(arr , used )
                    arr.pop()
                    del used[i]
                    
        permutations()
        return answer