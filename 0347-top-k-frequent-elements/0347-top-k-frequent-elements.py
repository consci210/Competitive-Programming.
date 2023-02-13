class Solution(object):
    def topKFrequent(self, nums, k):

        freq = Counter(nums)
    
        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
            
        return list(sorted_freq.keys())[:k]