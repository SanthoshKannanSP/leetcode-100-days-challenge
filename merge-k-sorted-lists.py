class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoList(head1,head2):
            start = None
            tail = None

            while head1 and head2:
                if head1.val < head2.val:
                    newNode = ListNode(head1.val)
                    head1 = head1.next
                else:
                    newNode = ListNode(head2.val)
                    head2 = head2.next
                if start is None:
                    start = newNode
                    tail = start
                else:
                    tail.next = newNode
                    tail = newNode
                
            while head1:
                newNode = ListNode(head1.val)
                if start is None:
                    start = newNode
                    tail = newNode
                else:
                    tail.next = newNode
                    tail = newNode
                head1 = head1.next
            
            while head2:
                newNode = ListNode(head2.val)
                if start is None:
                    start = newNode
                    tail = newNode
                else:
                    tail.next = newNode
                    tail = newNode
                head2 = head2.next

            return start

        if len(lists)==0:
            return None

        if len(lists)==1:
            return lists[0]

        ans = lists[0]

        mid = len(lists)//2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return mergeTwoList(left,right)