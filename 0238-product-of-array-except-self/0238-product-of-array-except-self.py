class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []
        answer = []
        product = 1
        for num in nums :
            product= product * num 
            left_product.append(product)
        product = 1
        for num in reversed(nums) :
            product= product * num 
            right_product.append(product)
        right_product.reverse()
        print(left_product , right_product)
        for i in range(len(left_product)):
            if i == 0:
                answer.append(right_product[1])
            elif i == len(left_product)-1 :
                answer.append(left_product[i-1])
            else :
                (answer.append(left_product[i-1] * right_product[i+1]))
                
        return answer 
         