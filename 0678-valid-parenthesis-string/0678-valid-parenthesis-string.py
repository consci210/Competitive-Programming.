class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        spare = []
        for i in range(len(s)):
            if s[i] == "(" :
                stack.append(i)
            elif s[i] == "*":
                spare.append(i)
            else :
                if stack :
                    stack.pop()
                elif spare :
                    spare.pop()
                else :
                    return False 
        while stack and spare :
            if stack[-1]  < spare[-1]:
                stack.pop()
                spare.pop()
            else :
                break 
                
        return len(stack) == 0