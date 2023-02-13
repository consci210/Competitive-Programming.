class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hashset = {}
        count = 0 
        length = len(arr)
        target = len(arr)//2 
        for num in arr : 
            if num in hashset.keys() :
                hashset[num]+= 1
            else :
                hashset[num] = 1
     
        value_key_pairs = ((value, key) for (key,value) in hashset.items())
        sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
        for value, key in sorted_value_key_pairs :
            if length > target :
                length -= (value)
                count += 1
        
        return count 
            