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
        
        index = 0

        while head:
            i = 0
            node = head
            x = node.next
            while i <= index and x != None:
                if x == node:
                    return True
                x = x.next
                i += 1

            head = head.next
            index += 1

        return False

        