class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        answer = []
        for key in count :
            answer.append([-1* count[key] , key ])   
        res = []
        heapq.heapify(answer)
        for i in range(k):
            res.append(heapq.heappop(answer)[1])
        
        return res