class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefixSum = 0
        d = dict()
        dummy = ListNode(0)
        dummy.next = head
        d[0] = dummy
        while head:
            prefixSum += head.val
            if prefixSum in d:
                start = d[prefixSum]
                p = start
                pSum = prefixSum
                while p != head:
                    p = p.next
                    pSum += p.val
                    if p!=head:
                        del d[pSum]
                start.next = head.next
            else:
                d[prefixSum] = head
            head = head.next
        return dummy.next