class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #using MinHeaps / Priority Queues
        values = []
        for point in points :
            values.append([ point[0]**2 + point[1]**2 , point[0] , point[1] ])
        
        heapq.heapify(values)
        answer = []
        while k :
            distance , x , y = heapq.heappop(values)
            answer.append( [x ,y]) 
            k-=1
            
        return answer
         
        
#         Using sorted lists 
#         list2 = sorted(points , key = lambda x : x[0]**2 + x[1]**2)  
#         return list2[:k:]