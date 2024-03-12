class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head.next
        pointer = head
        
        current_sum = 0

        while not node is None:
            if node.val == 0:
                pointer.next.val = current_sum
                pointer = pointer.next
                current_sum = 0
            else:
                current_sum += node.val

            node = node.next
        
        pointer.next=None
        return head.next