class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        neighbours = defaultdict(list)

        for course, prerequisite in prerequisites:
            indegree[course] += 1
            neighbours[prerequisite].append(course)

        queue = [i for i in range(numCourses) if indegree[i] == 0]
        ans = []
        visited = set()
        while queue:
            n = len(queue)
            for i in range(n):
                course = queue.pop(0)
                ans.append(course)
                visited.add(course)
                for j in neighbours[course]:
                    indegree[j] -= 1
            queue = [
                i for i in range(numCourses) if indegree[i] == 0 and i not in visited
            ]

        return [] if len(ans) < numCourses else ans
