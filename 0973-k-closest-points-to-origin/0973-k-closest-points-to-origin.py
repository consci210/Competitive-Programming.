class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        list2 = sorted(points , key = lambda x : x[0]**2 + x[1]**2)
   
        return list2[:k:]