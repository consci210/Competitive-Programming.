class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        stack2 = []
        for i in s:
            if i == ")":
                while True :
                    b = stack.pop()
                    if b == "(" :
                        break
                    stack2.append(b)
                stack.extend(stack2)
                stack2 = []
            else :
                stack.append(i)
        return "".join(stack)