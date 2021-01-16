# -*- coding: utf-8 -*-
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(0, head)
        first = pre
        second = pre
        for i in range(n):
            first = first.next
        
        while first.next != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        
        return pre.next