class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ns1 = set(nums1)
        ns2 = set(nums2)

        count1 = 0
        for i in nums1:
            if i in ns2:
                count1+=1
        
        count2 = 0
        for i in nums2:
            if i in ns1:
                count2+=1
        
        return [count1,count2]
