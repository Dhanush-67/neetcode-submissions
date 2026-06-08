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
        lst = []

        cur = head

        while cur:
            tmp = head
            index = 0

            if cur.random == None:
                index = -1
            else:
                while tmp != cur.random and tmp != None:
                    tmp = tmp.next
                    index += 1

            lst.append([cur, index])
            cur = cur.next

        new_head = Node(0, None, None)
        dummy = new_head
        lst2 = []
        for i in lst:
            tmp = Node(i[0].val, None, None)
            dummy.next = tmp
            lst2.append(tmp)
            dummy = dummy.next

        for i in range(len(lst)):
            if lst[i][1] == -1:
                lst2[i].random = None
            else:
                lst2[i].random = lst2[lst[i][1]]

        return new_head.next
