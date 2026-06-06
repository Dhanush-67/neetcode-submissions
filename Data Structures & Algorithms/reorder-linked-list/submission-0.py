# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return 

        cur = head

        lst = []

        while cur:
            lst.append(cur)
            cur = cur.next

        i = 0
        j = len(lst)-1

        while i < j:
            lst[i].next = lst[j]
            i += 1
            if i < j:
                lst[j].next = lst[i]
                j -= 1
        lst[j].next= None
        



        