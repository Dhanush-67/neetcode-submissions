# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root:
            return output

        stack = deque()

        stack.append(root)

        while stack:
            length = len(stack)
            mini_stack = []
            for i in range(length):
                node = stack.popleft()
                if node:
                    mini_stack.append(node.val)
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)

            output.append(mini_stack)
        return output
            

        