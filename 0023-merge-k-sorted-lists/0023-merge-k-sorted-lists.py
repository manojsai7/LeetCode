# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        while True:
            min_idx=-1
            for i in range(len(lists)):
                if lists[i]:
                    if min_idx==-1 or lists[i].val<lists [min_idx].val:

                        min_idx=i
            if min_idx==-1:
                break
            tail.next=lists[min_idx]
            tail=tail.next
            lists[min_idx]=lists[min_idx].next
        return dummy.next

