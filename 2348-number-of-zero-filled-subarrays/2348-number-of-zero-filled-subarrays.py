class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count , answer = 0 , 0 
        for num in nums :
            if num == 0 :
                count+=1 
            else :
                answer+= count*(count+1)//2
                count = 0
        if count :
            answer+= count*(count+1)//2
        return answer 
    
    