# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n steps
        for _ in range(n):
            fast = fast.next

        # Move both pointers
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the node
        slow.next = slow.next.next

        return dummy.next
