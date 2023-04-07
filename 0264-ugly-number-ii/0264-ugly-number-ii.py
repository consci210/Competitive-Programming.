class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        count = 0 
        seen = {} 
        store = []
        while True :
            nxt = [ugly[count]*2 , ugly[count]*3 , ugly[count]*5]
            for num in nxt :
                if num not in seen :
                    heapq.heappush(store,num)
            count+=1  
            found = False 
            while not found :
                small = heapq.heappop(store)
                if small not in seen :
                    heapq.heappush(ugly , small)
                    found = True 
                seen[small] = 1
            if count == n*3 :  
                return ugly[n-1]