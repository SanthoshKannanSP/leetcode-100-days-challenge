class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_tree(root,left_s,left_e,right_s,right_e):
            if left_s<=left_e:
                mid = left_s + ceil((left_e-left_s)/2)
                root.left = TreeNode(nums[mid])
                create_tree(root.left,left_s,mid-1,mid+1,left_e)
            if right_s<=right_e:
                mid = right_s + ceil((right_e-right_s)/2)
                root.right = TreeNode(nums[mid])
                create_tree(root.right,right_s,mid-1,mid+1,right_e)
            return

        s = 0
        e = len(nums)-1

        m = s + (e-s)//2
        root = TreeNode(nums[m])
        create_tree(root,s,m-1,m+1,e)

        return root