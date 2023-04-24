class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            "2" :"abc" , 
            "3" : "def" , 
            "4" : "ghi" ,
            "5" : "jkl" ,
            "6" : "mno" , 
            "7" : "pqrs" ,
            "8" : "tuv" , 
            "9" : "wxyz"
        }
        ans = []
        def backtrack(idx=0 , curr="") :
            if len(curr) == len(digits):
                ans.append(curr)
                return  
            for ch in  hashmap[digits[idx]]:
                backtrack(idx+1 , curr+ch)
        
        backtrack()
        return ans if digits else []
    