# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        if head.next == None:
            return False

        stack = set()

        while head:
            if head in stack:
                return True
            stack.add(head)
            head = head.next

        return False
        