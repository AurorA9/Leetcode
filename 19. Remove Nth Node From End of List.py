class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lastpoint = head  
        deletep = head  #指向前一个
        
        p = head
        lens = 0
        while(p):
            lens += 1
            p = p.next
        if lens == n:
            return head.next
        
        
        n = n+1
        while(n):
            n -= 1
            lastpoint = lastpoint.next
            
        while lastpoint:
            deletep = deletep.next
            lastpoint = lastpoint.next
        deletep.next = deletep.next.next
            
        return head