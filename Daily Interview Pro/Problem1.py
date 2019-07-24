##Problem Statement-  Given two sorted linked lists, merge them in order...

class ListNode(object):
    def __init__(self,x):
        self.val= x
        self.next= None

class Solution:
    def mergeTwoLists(self,l1,l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next= self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next= self.mergeTwoLists(l1,l2.next)
            return l2

#Test Program
a=ListNode(1)
a.next=ListNode(3)
a.next.next=ListNode(5)

b=ListNode(2)
b.next=ListNode(4)
b.next.next=ListNode(6)

c=Solution().mergeTwoLists(a, b)
while c:
    print(c.val)
    c=c.next
