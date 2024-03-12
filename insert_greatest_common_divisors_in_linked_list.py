# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current.next:
            node = ListNode(math.gcd(current.val,current.next.val))
            node.next = current.next
            current.next = node
            current = node.next
            

        return head