
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        refLast = None
        refList1 = list1
        refList2 = list2
        while refList1 is not None or refList2 is not None:
            if refList1 is None:
                new = ListNode(refList2.val)
                refList2 = refList2.next
            elif refList2 is None:
                new = ListNode(refList1.val)
                refList1 = refList1.next
            elif refList1.val <= refList2.val:
                new = ListNode(refList1.val)
                refList1 = refList1.next
            elif refList1.val > refList2.val:
                new = ListNode(refList2.val)
                refList2 = refList2.next
            if refLast is not None:
                refLast.next = new
            refLast = new
            if head is None:
                head = refLast
        return head

solution = Solution()

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

print(solution.mergeTwoLists(list1, list2))