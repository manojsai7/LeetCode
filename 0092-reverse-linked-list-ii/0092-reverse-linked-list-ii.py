# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        before=dummy
        for i in range(left-1):
            before=before.next
        cur=before.next
        for i in range(right-left):
            temp=cur.next
            cur.next=temp.next
            temp.next=before.next
            before.next=temp
        return dummy.next







        

        