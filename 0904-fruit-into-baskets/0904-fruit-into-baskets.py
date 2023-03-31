class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
    # length - longest == k
        maximum = 0 
        hashmap = {}
        l = 0 
        r = 0
        while r < len(fruits) :
            hashmap[fruits[r]] = hashmap.get(fruits[r] , 0 ) + 1
            
            while len(hashmap) > 2 :
                hashmap[fruits[l]] -= 1
                if hashmap[fruits[l]] == 0 :
                    del hashmap[fruits[l]]
                l+=1
            current_sum = sum(hashmap.values())  
            maximum = max(maximum , current_sum)
            r+=1 
         
        return maximum 
    