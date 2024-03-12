class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        cumsum = [0,travel[0]]
        for i in range(1,len(travel)):
            cumsum.append(cumsum[-1]+travel[i])
        
        lastpos = defaultdict(int)
        count = defaultdict(int)
        gtypes = ["M","G","P"]
        for house in range(len(garbage)):
            for gtype in gtypes:
                if gtype in garbage[house]:
                    lastpos[gtype] = house
                    count[gtype] += garbage[house].count(gtype)
        return sum([count[gtype]+cumsum[lastpos[gtype]] for gtype in gtypes if gtype in lastpos])