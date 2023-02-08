class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    # Efficient solution 
        l = 0
        r = len(nums)-1
        newArray = []
        while l<= r :
            num1 = nums[l]**2
            num2 = nums[r]**2
            if num1 >= num2 :
                newArray.append(num1)
                l+=1
            else :
                newArray.append(num2)
                r-=1
        newArray.reverse()
        return newArray

    #  Brute force solution O(nlogn)
        # lenOfArray = len(nums)
        # newArray = []
        # for i in range(lenOfArray) :
        #     newArray.append((nums[i])**2)
        # newArray.sort()
        # return newArray

