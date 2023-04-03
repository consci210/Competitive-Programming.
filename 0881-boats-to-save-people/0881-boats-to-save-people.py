class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = l = 0 
        r = len(people)-1
        while l <= r :
            if people[l]+people[r] <= limit :
                boat +=1 
                l+=1
                r-=1
            else :
                r-=1
                boat +=1 
                
        return boat 