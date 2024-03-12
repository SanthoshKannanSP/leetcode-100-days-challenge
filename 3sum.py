class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos,neg,zero = defaultdict(int),defaultdict(int),0

        for num in nums:
            if num>0:
                pos[num]+=1
            elif num<0:
                neg[num]+=1
            else:
                zero+=1

        res = []
        
        if zero>=3:
            res.append((0,0,0))
        
        plist,nlist = list(pos),list(neg)
        pset,nset = set(plist),set(nlist)
        np,nn = len(plist),len(nlist)
        for i in range(np):
            for j in range(i,np):
                n,m = plist[i],plist[j]
                if n==m and pos[n]<2:
                    continue
                if -n-m in nset:
                    res.append((n,m,-n-m))

        for i in range(nn):
            if -nlist[i] in plist and zero>0:
                res.append((nlist[i],0,-nlist[i]))
            for j in range(i,nn):
                n,m = nlist[i],nlist[j]
                if n==m and neg[n]<2:
                    continue
                if -n-m in pset:
                    res.append((n,m,-n-m))

        return res