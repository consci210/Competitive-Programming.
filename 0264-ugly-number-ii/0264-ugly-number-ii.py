class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        count = 0 
        seen = {} 
        store = []
#         1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36
        while True :
            nxt = [ugly[count]*2 , ugly[count]*3 , ugly[count]*5]
            for num in nxt :
                if num not in seen :
                    store.append(num)
            count+=1  
            found = False 
            while not found :
                small = heapq.heappop(store)
                if small not in seen :
                    ugly.append(small)
                    found = True 
                seen[small] = 1
            if count == n*3 :
                ugly.sort()
                print(ugly)
                return ugly[n-1]