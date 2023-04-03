class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1 :
            return stones[0]
        stones = [-num for num in stones ]
        heapq.heapify(stones)
        while len(stones) > 1 :
            first = heapq.heappop(stones)
            second =  heapq.heappop(stones)     
            diff = first - second 
            if diff < 0 :
                heapq.heappush(stones , diff)
        
        return stones[0]*-1 if stones else 0 
    
        