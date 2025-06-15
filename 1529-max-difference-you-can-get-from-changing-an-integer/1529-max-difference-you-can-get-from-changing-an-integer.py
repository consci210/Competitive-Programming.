class Solution:
    def maxDiff(self, num: int) -> int:
        number = str(num)
        x = set(number)
        small = str(num)
        large = str (num)
        for i in range(0,10):
            for j in x:
                if number[0] != j or i != 0:
                    curr = number.replace(j,str(i))
                    small = str(min(int(curr),int(small)))
                    large = str(max(int(curr),int(large)))
        return (int(large)- int(small))