class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for directory in path.split("/") :
            if directory == "" :
                pass
            elif directory == ".." :
                if stack :
                    stack.pop()
            elif directory == "." :
                pass 
            else :
                stack.append(directory)
                
        answer = "/" + "/".join(stack)
        return answer