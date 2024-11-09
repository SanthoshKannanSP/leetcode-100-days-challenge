class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stopToBus = defaultdict(list)

        for bus, route in enumerate(routes):
            for stop in route:
                stopToBus[stop].append(bus)

        if source==target:
            return 0

        if source not in stopToBus or target not in stopToBus:
            return -1

        q = deque([source])
        busVisited = set()
        stopVisited = set()
        ans = 0

        while q:
            ans+=1
            n = len(q)

            for _ in range(n):
                curr = q.popleft()

                for bus in stopToBus[curr]:
                    if bus in busVisited:
                        continue
                    busVisited.add(bus)

                    for stop in routes[bus]:
                        if stop==target:
                            return ans

                        q.append(stop)
                        stopVisited.add(stop)

        return -1