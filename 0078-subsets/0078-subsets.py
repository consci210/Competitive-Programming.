class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        N = len(nums)
        def backtrack( idx , arr ) :
            
            for i in range(idx , N):
                arr.append(nums[i])
                backtrack(i+1 ,arr)
                answer.append(arr.copy())
                arr.pop()
        backtrack(0 , [])    
        return answer 