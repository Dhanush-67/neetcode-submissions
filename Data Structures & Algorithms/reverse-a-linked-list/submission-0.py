# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0, None)
        flag = 0


        if head == None:
            return head


        while head != None:
            if flag == 0:
                node = None
            else:
                node = ListNode(new_head.val, new_head.next)
            new_head.val = head.val
            new_head.next = node
            head = head.next
            flag = 1
        
        return new_head
        