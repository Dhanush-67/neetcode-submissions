# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0,None)
        cur = head
        carry = 0

        while l1 != None and l2 != None:
            if carry:
                value = l1.val+l2.val+1
                carry = 0
            else:
                value = l1.val + l2.val
            if value > 9:
                carry = 1
                value = value%10

            cur.next = ListNode(value, None)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            if carry:
                value = l1.val+1
                carry = 0
            else:
                value = l1.val
            if value > 9:
                carry = 1
                value = value%10

            cur.next = ListNode(value, None)
            cur = cur.next
            l1 = l1.next

        while l2 != None:
            if carry:
                value = l2.val+1
                carry = 0
            else:
                value = l2.val
            if value > 9:
                carry = 1
                value = value%10

            cur.next = ListNode(value, None)
            cur = cur.next
            l2 = l2.next


        if carry:
            cur.next = ListNode(carry,None)

        return head.next
        