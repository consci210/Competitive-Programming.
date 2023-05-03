class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack = []
        free = []
        
        for i in range(len(s)) :   
            if locked[i] == "0":
                free.append(i)
            elif s[i] == "(":
                stack.append(i)
            else :
                if stack :
                    stack.pop()
                elif free :
                    free.pop()
                else:
                    return False 
                
        while stack and free:
            if stack[-1] < free[-1]:
                stack.pop()
                free.pop()
            else:
                break 
                
        return len(stack) == 0 and len(free)%2 == 0
            
            