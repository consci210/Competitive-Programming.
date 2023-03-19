class Solution:
    def decodeString(self, s: str) -> str :
        stack = []
        multiplicity = []
        num = ""
        for character in s :
            if character.isnumeric() :
                num+=character 
            elif character == "]" :
                ans = []
                while stack[-1] != "[" :   
                    ans.append(stack.pop()) 
                stack.pop()
                ans.reverse()
                for i in range(int(multiplicity.pop())):
                    stack.extend(ans)
            else :
                if character == "[" :
                    multiplicity.append(int(num))
                    num = ""        
                stack.append(character)
        return "".join(stack)