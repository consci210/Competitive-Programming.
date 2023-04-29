class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]: 
        answer = []
        def backtrack(idx=0 , curr=[]):    
            answer.append(curr.copy())
            for i in range(idx , len(nums)):
                curr.append(nums[i])
                backtrack(i+1 , curr)
                curr.pop()            
        backtrack()
        return answer