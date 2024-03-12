class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        val = 1
        for index in range(len(target)):
            while val!=target[index]:
                val+=1
                ans.append("Push")
                ans.append("Pop")
            ans.append("Push")
            val+=1

        return ans