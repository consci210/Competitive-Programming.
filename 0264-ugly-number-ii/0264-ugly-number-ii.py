class Solution:
    def nthUglyNumber(self, n: int) -> int:   
            index2 = index3 = index5 = 0 
            ugly_numbers = [1]
            while len(ugly_numbers) < n :
                current_ugly_numbers = [ugly_numbers[index2]*2 , ugly_numbers[index3]*3 , ugly_numbers[index5]*5 ] 
                heapq.heapify(current_ugly_numbers)
                smallest_ugly_number = heapq.heappop(current_ugly_numbers)
                heapq.heappush(ugly_numbers , smallest_ugly_number)
                if smallest_ugly_number == ugly_numbers[index2]*2 :
                    index2+=1
                if  smallest_ugly_number == ugly_numbers[index3]*3 :
                    index3+=1
                if  smallest_ugly_number == ugly_numbers[index5]*5 :
                    index5+=1
            
            
            return (ugly_numbers[n-1])
                