class Solution:
    def nthUglyNumber(self, n: int) -> int:
            
            index2 = index3 = index5 = 0 
            ugly_numbers = [1]
            while len(ugly_numbers) < n :
                smallest_ugly_number = min( ugly_numbers[index2]*2 , ugly_numbers[index3]*3 , ugly_numbers[index5]*5  )   
                ugly_numbers.append(smallest_ugly_number)
                
                if ugly_numbers[-1] == ugly_numbers[index2]*2 :
                    index2+=1
                if ugly_numbers[-1] == ugly_numbers[index3]*3 :
                    index3+=1
                if ugly_numbers[-1] == ugly_numbers[index5]*5 :
                    index5+=1
            
            return ugly_numbers[-1]
                