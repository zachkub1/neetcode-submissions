"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        graph = {}
        q = deque([node])
        seen = set()

        while q:
            curr = q.popleft()

            if curr in seen:
                continue
            seen.add(curr)

            if curr not in graph:
                graph[curr] = Node(curr.val)

            for neigh in curr.neighbors:
                if neigh not in graph:
                    graph[neigh] = Node(neigh.val)
                graph[curr].neighbors.append(graph[neigh])
                q.append(neigh)
        return graph[node]
            


