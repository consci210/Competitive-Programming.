class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        array = [i for i in range(1,n+1)]
        def backtrack(i , arr) :
            if len(arr) == k :   
                answer.append(arr.copy())
                return 
            if i >= len(array):
                return 
            
            choice = array[i]
            #take
            arr.append(choice)
            backtrack(i+1,arr)
            #not take 
            arr.pop()
            backtrack(i+1 ,arr)
        
        backtrack(0,[])
        return answer 