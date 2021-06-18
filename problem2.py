# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.result = 0
        def helper(root, currSum):
            if root == None:
                return
            currSum = currSum*10 + root.val
            helper(root.left, currSum)
            #stack.pop() for the left call happens here
            if (root.left == None and root.right == None): self.result += currSum
            helper(root.right, currSum)
            #stack.pop() for the right call happens here
            
        helper(root,0)
        return self.result
    
#Time complexity is O(n) 
#Space complexity is O(h) 
#Inorder traversal with current sum as local variable for the helper function summed up at each leaf node
            
            