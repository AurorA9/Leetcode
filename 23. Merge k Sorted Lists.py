合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#分而治之
#链表两两合并
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return 
        lens = len(lists)
        return self.merge(lists,0,lens-1)
    def merge(self,lists,left,right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2 
        l1 = self.merge(lists,left,mid)
        l2 = self.merge(lists,mid+1,right)
        return self.mergeTwoList(l1,l2)
    def mergeTwoList(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoList(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoList(l1,l2.next)
            return l2
        
        