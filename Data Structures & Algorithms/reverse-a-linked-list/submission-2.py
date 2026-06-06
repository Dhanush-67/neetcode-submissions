# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        if head == None:
            return None

        traverse = head

        while traverse:
            if not node:
                node = ListNode(traverse.val, None)
            else:
                new_node = ListNode(traverse.val, node)
                node = new_node
            traverse = traverse.next
        
        return node