# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None

        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        head = prev
        prev = None
        cur = head

        i = 1

        while i != n:
            prev = cur
            cur = cur.next
            i += 1
        
        if prev == None and cur.next == None:
            return None
        if prev == None and cur.next != None:
            head = cur.next
        else:
            prev.next = cur.next
            cur.next = None

        prev = None

        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev