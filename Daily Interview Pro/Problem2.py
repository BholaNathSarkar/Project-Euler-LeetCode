# Problem: You are given two linked-lists representing two non-negative integers.
#       The digits are stored in reverse order and each of their nodes contain a single digit.
#       Add the two numbers and return it as a linked list.
#       Example:Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#               Output: 7 -> 0 -> 8
#               Explanation: 342 + 465 = 807.

#Pseudocode:     1.Initialize current node to dummy head of the returning list.
#                2.Initialize carry to 0.
#                3.Initialize p and q to head of l1 and l2 respectively.
#                4.Loop through lists l1 and l2 until you reach both ends.
#                5.Set x to node p's value. If p has reached the end of l1, set to 0.
#                6.Set y to node q's value. If q has reached the end of l2, set to 0.
#                7.Set sum = x + y + carry
#                8.Update carry = sum / 10.
#                9.Create a new node with the digit value of (sum mod 10) and set it to
#                   current node's next, then advance current node to next.
#                10.Advance both p and q.
#                11.Check if carry = 1, if so append a new node with digit 1 to the returning list.
#                   Return dummy head's next node


#Definition of singly-linked list.
class ListNode(object):
    def __init__(self,x):
        self.val= x
        self.next=None

class Solution:
    def addTwoNumbers(self,l1,l2,carry=0):
        sum=l1.val+l2.val+carry
        carry=sum//10
        result=ListNode(sum % 10)

        if(l1.next !=None or l2.next !=None or carry!=0):
            if(l1.next == None):
                l1.next=ListNode(0)
            if(l2.next == None):
                l2.next=ListNode(0)
            result.next=self.addTwoNumbers(l1.next,l2.next,carry)
        return result
#Test Program
a=ListNode(2)
a.next=ListNode(4)
a.next.next=ListNode(3)

b=ListNode(5)
b.next=ListNode(6)
b.next.next=ListNode(4)

c=Solution().addTwoNumbers(a,b)
while(c):
   print(c.val)
   c=c.next
