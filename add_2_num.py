# -*- coding: utf-8 -*-
'''
Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution: # Normal method
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        re = result
        carry = 0
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0 
            s = carry + x + y
            carry = s//10
            re.next = ListNode(s % 10)
            re = re.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry > 0:
            re.next = ListNode(1)
        return result.next
    
class Solution2: # 递归解法
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def dfs(l, r, i):
            if not l and not r and not i: return None
            s = (l.val if l else 0) + (r.val if r else 0) + i
            node = ListNode(s % 10)
            node.next = dfs(l.next if l else None, r.next if r else None, s // 10)
            return node
        return dfs(l1, l2, 0)