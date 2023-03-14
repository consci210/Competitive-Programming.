class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        for bracket in s :
            if (bracket == "(") or (bracket == "{") or ( bracket =="[") :
                stack.append(bracket)
            elif bracket == ")" :
                if stack :
                    last_bracket = stack.pop()
                    if last_bracket != "(" :
                        return False 
                else :
                    return False 
                     
            elif bracket == "}" :
                if stack :
                    last_bracket = stack.pop()
                    if last_bracket != "{" :
                        return False
                else :
                    return False 
            elif bracket == "]" :
                if stack :
                    last_bracket = stack.pop()
                    if last_bracket != "[" :
                          return False 
                else :
                    return False 
        if not stack :
            return True 
        else :
            return False 
            
            