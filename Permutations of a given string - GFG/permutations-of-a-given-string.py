#User function Template for python3

class Solution:
    def find_permutation(self,S):
        result = [] 
        chars = sorted(list(S))  
        def permute(start, end):
            if start == end:
               
                result.append(''.join(chars))
            else:
                visited = set()  
                for i in range(start, end + 1):
                    if chars[i] in visited:
                        continue 
                    visited.add(chars[i])
                   
                    chars[start], chars[i] = chars[i], chars[start]
                   
                    permute(start + 1, end)
                    
                    chars[start], chars[i] = chars[i], chars[start]
    
        permute(0, len(chars) - 1)  
        return sorted(result)




#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends