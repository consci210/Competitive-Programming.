class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def backtrack(i , target , arr):
            if target == 0 :
                answer.append(list(arr))
                return 
            if i >= len(candidates) or  target < 0 :
                return 
            
            choice = candidates[i]
            arr.append(choice)
            backtrack(i , target-choice , arr )
            arr.pop()
            backtrack(i+1 , target , arr)
            
            return answer 

        backtrack(0 , target , [])
        return answer
