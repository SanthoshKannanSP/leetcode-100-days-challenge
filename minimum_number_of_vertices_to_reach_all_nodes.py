class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0]*n

        for source, destination in edges:
            in_degree[destination] += 1

        return [i for i in range(n) if in_degree[i]==0]