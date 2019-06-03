给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。


class Solution
    def canJump(self, nums List[int]) - bool
        
        #自己写的，每次求解获得利益最大的坐标 利益：max(当前坐标结果 + 坐标index) 
#         poi = 0
#         lens = len(nums) - 1
#         while poi  lens 
            
#             now_num = nums[poi]
#             if now_num == 0 and poi == lens
#                 return True
#             elif now_num == 0 and poi != lens
#                 return False
#             elif now_num + poi = lens
#                 return True
#             else
#                 maxi = -1
#                 max_num = -1
#                 for i in range(1,now_num+1)
#                     if nums[poi + i] + i = max_num + maxi
#                         maxi =  i
#                         max_num = nums[poi + i]
#                 poi = maxi + poi
               
#         return poi == lens
        #别人
        max_ = 0
        for i in range(len(nums))
            if max_ =i
                max_ = max(max_,i+nums[i])
            else
                return False   
        if max_ = len(nums)-1
            return True
        else
            return False