# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root, Ans):
    if root == None:
        return 
    inorder(root.left, Ans)
    Ans.append(root.val)
    inorder(root.right,Ans)
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        stack = []
        inorder(root,stack)
        diff = max(stack)
        for i in range(len(stack) - 1):
            diff = min(diff,stack[i+1] - stack[i])
        return diff