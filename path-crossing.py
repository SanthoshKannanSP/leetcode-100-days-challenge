class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y = 0,0
        visited = set()
        visited.add((x,y))

        for d in path:
            if d=="N":
                x+=1
            elif d=="S":
                x-=1
            elif d=="E":
                y+=1
            elif d=="W":
                y-=1
            if (x,y) in visited:
                return True
            visited.add((x,y))

        return False