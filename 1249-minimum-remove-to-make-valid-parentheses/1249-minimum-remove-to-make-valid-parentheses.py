class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        l = list(s)
        for i in range(len(s)):
            if l[i] == "(" :
                stack.append(i)
            elif l[i] == ")" :
                if stack :
                    stack.pop()
                else :
                    l[i] = ""
        while stack :
            ch = stack.pop()
            l[ch] = ""
            
        return "".join(l)