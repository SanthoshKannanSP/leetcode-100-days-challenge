# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        sorted1 = []
        sorted2 = []

        def inorder(root,n):
            if root is None:
                return
            inorder(root.left,n)
            if n==1:
                sorted1.append(root.val)
            else:
                sorted2.append(root.val)
            inorder(root.right,n)
            return

        inorder(root1,1)
        inorder(root2,2)

        i,j = 0,0
        n,m = len(sorted1),len(sorted2)
        ans = []
        
        while i<n and j<m:
            if sorted1[i]<sorted2[j]:
                ans.append(sorted1[i])
                i+=1
            else:
                ans.append(sorted2[j])
                j+=1
        while i<n:
            ans.append(sorted1[i])
            i+=1
        while j<m:
            ans.append(sorted2[j])
            j+=1
        return ans