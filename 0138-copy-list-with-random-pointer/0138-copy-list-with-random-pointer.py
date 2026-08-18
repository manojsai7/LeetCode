"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        org={}
        cur=head
        while cur:
            org[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            org[cur].next=org.get(cur.next)
            org[cur].random=org.get(cur.random)
            cur=cur.next
        return org[head]




        