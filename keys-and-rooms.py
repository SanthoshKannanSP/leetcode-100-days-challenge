class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [i for i in rooms[0]]
        visited = set([0])

        while stack:
            room = stack.pop()
            if room in visited:
                continue
            else:
                visited.add(room)
                for i in rooms[room]:
                    stack.append(i)

        return len(rooms) == len(visited)