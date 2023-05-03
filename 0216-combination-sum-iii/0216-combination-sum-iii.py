class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(idx=1 , curr=[] , total= 0 ):
            if len(curr) == k :
                if total == n :
                    res.append(curr.copy())
                return 
            if total > n :
                return 
            
            for i in range(idx,n):
                if i > 9 :
                    break
                curr.append(i)
                total+=i 
                backtrack(i+1 , curr , total)
                curr.pop()
                total-=i 
                
        backtrack()
        return res