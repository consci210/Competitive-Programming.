class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        answer = []
        
        def backtrack(i , total , arr):
            if total == 0 :
                answer.append(arr.copy())
                return 
            if total < 0 :
                return 
            prev = -1 
            for j in range(i , N):
                if total == 0 :
                    answer.append(arr.copy())
                    break  
                if candidates[j] == prev :
                    continue 
                arr.append(candidates[j])
                backtrack(j+1 , total- candidates[j] ,arr )
                arr.pop()
                prev = candidates[j]
        backtrack(0 , target , [])
        return answer