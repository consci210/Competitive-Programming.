#User function Template for python3

class Solution:
    def find_permutation(self,S):
        result = []  # Result vector to store permutations
        chars = sorted(list(S))  # Convert string to sorted character array

    # Recursive function to find permutations
        def permute(start, end):
            if start == end:
                # Reached the end of a permutation, add to result
                result.append(''.join(chars))
            else:
                visited = set()  # Set to track visited characters
                for i in range(start, end + 1):
                    if chars[i] in visited:
                        continue  # Skip redundant characters
                    visited.add(chars[i])
                    # Swap characters
                    chars[start], chars[i] = chars[i], chars[start]
                    # Recursively permute the remaining characters
                    permute(start + 1, end)
                    # Restore the original order by swapping back
                    chars[start], chars[i] = chars[i], chars[start]
    
        permute(0, len(chars) - 1)  # Start the permutation from index 0
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