class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for node,neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)
        stack = [source]
        visited = set()
        while stack:
            curr = stack.pop(-1)
            if curr in visited:
                continue
            if curr == destination :
                return True 
            stack+= graph[curr]
            visited.add(curr)
        return False 

