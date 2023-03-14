class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        l = [0 for _ in range(len(s))]
        
        for (index,character) in enumerate(s) :
            if character == "(":
                stack.append(index)
            else :
                if stack :
                    ok_index = stack.pop()
                    l[ok_index] = 1
                    l[index] = 1  
                 
        count , answer = 0 , 0        
        for i in range(len(s)):
            if l[i] == 1 :
                count +=1 
            else :
                count = 0 
            answer = max(count , answer)
        
        
        
        return (answer)