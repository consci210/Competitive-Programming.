class Solution:
    def decodeString(self, s: str) -> str :
        stack = []
        multiplicity = []
        num = ""
        for character in s :
            if character.isnumeric() :
                num += character 
            elif character == "]" :
                ans = []
                while stack[-1] != "[" :   
                    ans.append(stack.pop()) 
                stack.pop()
                ans.reverse()
                decoded = "".join(ans)
                stack.append(decoded * multiplicity.pop())
            else :
                if character == "[" :
                    multiplicity.append(int(num))
                    num = ""        
                stack.append(character)
        return "".join(stack)