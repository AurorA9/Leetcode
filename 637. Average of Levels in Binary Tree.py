给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        queue = [root]
        while queue:
            sum = 0
            lens = len(queue)
            for i in range(lens):
                node = queue.pop(0)
                
                sum += node.val
                if node.left !=None:
                    queue.append(node.left)
                if node.right !=None:
                    queue.append(node.right)
            ans.append(sum/lens)
        return ans