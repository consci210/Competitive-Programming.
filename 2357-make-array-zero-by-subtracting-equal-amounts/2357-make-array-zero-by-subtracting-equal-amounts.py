class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums =  filter(lambda x: (x != 0), nums)
        hashmap = defaultdict(int)
        for  num in nums :
            hashmap[num] += 1
        return len(hashmap)