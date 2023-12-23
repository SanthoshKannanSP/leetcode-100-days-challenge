class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index = {
            "type":0,
            "color":1,
            "name":2
        }

        index = index[ruleKey]
        count = 0

        for item in items:
            if item[index]==ruleValue:
                count+=1

        return count