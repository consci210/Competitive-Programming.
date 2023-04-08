class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heapq.heapify(matrix)
        for i in range(k) :
            smaller_arr = heapq.heappop(matrix)
            if smaller_arr :
                ans = heapq.heappop(smaller_arr)
            if smaller_arr :
                heapq.heappush(matrix , smaller_arr)
                
        return ans 