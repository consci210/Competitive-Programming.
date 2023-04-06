class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        array = [[ mat[i] , i ] for i in range(len(mat))]
        heapq.heapify(array) 
        answer = []
        for i in range(k):
            item , index = heapq.heappop(array)
            answer.append(index)
        return answer