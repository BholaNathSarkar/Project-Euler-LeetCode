"""
Problem Statement:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        list1=[]
        list2=[]
        while(l1):
            list1.append(l1.val)
            l1=l1.next
        while(l2):
            list2.append(l2.val)
            l2=l2.next
        a="".join(map(str,list1))
        a=int(a[::-1])
        b="".join(map(str,list2))
        b=int(b[::-1])
        c=a+b
        return Solution.to_list(c)
    def to_list(n: int):
        s = str(n)[::-1]
        head = prev = None
        for ch in s:
            node = ListNode(int(ch))
            if prev is not None:
                prev.next = node
            prev = node
            if head is None:
                head = prev
        return head
