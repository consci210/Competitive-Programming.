class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{" 
        }
        stack = []
        for i in range(len(s)):
            if s[i] not in pairs  :
                stack.append(s[i])
            else :
                if stack :
                    last = stack.pop()
                    if pairs[s[i]] != last :
                        return False 
                else :
                    return False 
        return True if not stack else False 