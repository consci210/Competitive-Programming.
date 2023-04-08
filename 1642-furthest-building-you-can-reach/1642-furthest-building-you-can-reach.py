class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff = []
        count = 0 
        for i in range(1,len(heights)) :
            gap = heights[i] - heights[i-1] 
            if gap > 0 :    
                diff.append(gap)
            else :
                diff.append(0)
        lad = []
        current_sum = 0
        sum_lad = 0
        for i in range(len(diff)) :
            current_sum += diff[i]
            if len(lad) < ladders :
                heapq.heappush(lad , diff[i] )
                sum_lad += diff[i]
            else :
                if lad and lad[0] < diff[i] :
                    sum_lad -= lad[0]
                    sum_lad += diff[i]
                    heapq.heappop(lad)
                    heapq.heappush(lad , diff[i])
                   
            if (current_sum - sum_lad) > bricks :
                return i
            
        return len(heights)-1