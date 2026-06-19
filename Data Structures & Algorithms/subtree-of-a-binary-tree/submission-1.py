# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, p, q):
        if p == q:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False

        left = self.check(p.left,q.left)
        right = self.check(p.right,q.right)

        if left and right and p.val == q.val:
            return True
        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == subRoot:
            return True
        if root == None:
            return False
        if root.val == subRoot.val:
            x = self.check(root, subRoot)
            if x:
                return True

        isLeft = self.isSubtree(root.left, subRoot)
        isRight = self.isSubtree(root.right, subRoot)

        return isLeft or isRight

        