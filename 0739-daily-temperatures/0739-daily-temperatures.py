class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair of temp and its index 
        answer = [0]*len(temperatures)
        for index , temp in enumerate(temperatures) :  # (0,73) (1,74)
            while stack and temp > stack[-1][1] :
                stackIndex , stackTemp = stack.pop()
                answer[stackIndex] = index - stackIndex 
            stack.append([index, temp])
        return answer 