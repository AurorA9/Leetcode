给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        ans = []
        while queue:
            temp = []
            for i in range(len(queue)):
                nowNode = queue.pop(0)
                temp.append(nowNode.val)
                if nowNode.left != None:
                    queue.append(nowNode.left)
                if nowNode.right != None:
                    queue.append(nowNode.right)
            ans.append(temp)
        return ans[::-1]
                