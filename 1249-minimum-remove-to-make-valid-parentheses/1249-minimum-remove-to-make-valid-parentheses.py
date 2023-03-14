class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        is_ok = [0 for _ in range(len(s))]
        stack = []
        for (i , letter) in enumerate(s) :
            if (letter =="("):
                stack.append(i)
            elif (letter == ")"):
                if stack :
                    ok_open = stack.pop()
                    is_ok[ok_open] = 1 
                    is_ok[i] = 1
                
        answer = ""
        for (i,letter) in enumerate(s) :
            if letter in "()":
                if is_ok[i] == 1 :
                    answer+=letter
            else :
                answer+= letter 
        
        return answer 
                    
            
                    