class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []   
        popped.reverse()
        for num in pushed :
            stack.append(num)
            if stack[-1] == popped[-1] :
                while stack and stack[-1] == popped[-1]:
                    stack.pop()
                    popped.pop()
        while stack :
            if stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()   
            if stack and stack[-1]!= popped[-1]:
                return False 
        return True 