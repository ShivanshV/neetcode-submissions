class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root,depth):
            if not root:
                return None
            if len(res) == depth:
                res.append(root.val)
            
           
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)

         
        
        dfs(root, 0)
        return res