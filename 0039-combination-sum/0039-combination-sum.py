class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(i=0 , curr=[] , total=0 ):
            if total == target :
                answer.append(curr.copy()) 
            if total >= target or i >= len(candidates) :
                return 
            
            #pick
            num = candidates[i]
            curr.append(num)
            backtrack(i , curr ,total+num )
            #not pick 
            curr.pop()
            backtrack(i+1 , curr ,total )
            
        backtrack()
        return answer 