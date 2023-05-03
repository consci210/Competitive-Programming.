class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []
        def generate( curr = "(" , op=1 , cl=0 ):
            
            if op > n :
                return 
            
            if cl > op :
                return 
            
            if len(curr) == 2*n:
                answer.append(curr)  
                   
            generate(curr +"(" , op+1 , cl)
            generate(curr+")" , op , cl+1)
            
        generate()
        return answer 