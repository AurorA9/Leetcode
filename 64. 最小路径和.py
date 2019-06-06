给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        ans = grid[0]
        for i in range(0,m):
            for j in range(n):
                if i == 0 and j ==0:
                    ans [j] = grid[0][0]
                    continue
                if i == 0:
                    ans[j] = grid[i][j] + ans[j-1]
                    continue
                if j == 0:
                    ans[j] = ans[j]+grid[i][j]
                    continue
                
                ans[j] = min(ans[j]+grid[i][j],ans[j-1]+grid[i][j])
            
        return ans[-1]