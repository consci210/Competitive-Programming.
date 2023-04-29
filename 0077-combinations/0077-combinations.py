class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        
        def backtrack(idx=1 , curr=[]):
            
            if len(curr) == k  :
                answer.append(curr.copy())
                return 
            
            for i in range(idx , n+1):
                curr.append(i)
                backtrack(i+1 , curr)
                curr.pop()
                
      
        backtrack()
        return answer 