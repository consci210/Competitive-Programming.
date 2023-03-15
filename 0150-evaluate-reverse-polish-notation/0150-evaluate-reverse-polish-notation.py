import operator 
class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        operators = {
            "+" : operator.add ,
            "-" : operator.sub ,
            "*" : operator.mul ,
            "/" : operator.truediv 
        }
        
        for token in tokens :
            if token in operators :
                num2 = int(stack.pop())
                num1= int(stack.pop())
                answer = operators[token](num1,num2)
                stack.append(answer)     
            else :
                stack.append(token)
        return int(stack[0])