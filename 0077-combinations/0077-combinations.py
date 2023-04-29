class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        
        def backtrack(idx=1 , curr=[]):
            
            if len(curr) == k  :
                answer.append(curr.copy())
                return 
            if idx > n :
                return 
            
            curr.append(idx)
            backtrack(idx+1 ,curr)
            curr.pop()
            backtrack(idx +1, curr)
        backtrack()
        return answer 