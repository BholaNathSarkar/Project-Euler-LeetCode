# Problem : Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

#Solution:

#Node Class
class Node:

    #constructor to initiate the node object
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    #Function to initialize head
    def __init__(self):
        self.head=None

    #Function to reverse the Linked List-ITERATIVE Approach
    def iterativeReverse(self):
        current=self.head
        prev=None
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev


  #Function to reverse the LinkedList- RECURSIVE Approach
    def reverseUtil(self, curr, prev):

       #If last Node, then Mark is head
       if curr.next is None:
           self.head=curr
           curr.next=prev
           return

      #save curr.next for recursive call and update next
       next=curr.next
       curr.next=prev

       self.reverseUtil(next, curr)

    def recursiveReverse(self):
       if self.head is None:
           return
       self.reverseUtil(self.head, None)


   #Function to insert a new node in the beginning
    def push(self, new_data):
       new_node=Node(new_data)
       new_node.next=self.head
       self.head=new_node

   #Function to print the linked List
    def printList(self):
       temp=self.head
       while(temp):
           print(temp.data)
           temp=temp.next

#Test Program -iterative
list1=LinkedList()
list1.push(3)
list1.push(5)
list1.push(7)
print("Given Linked list: ")
list1.printList()
print("Reverse Linked List: ")
list1.iterativeReverse()
list1.printList()

#Test Program -recursive
list2=LinkedList()
list2.push(9)
list2.push(6)
list2.push(3)
print("Given Linked list: ")
list2.printList()
print("Reverse Linked List: ")
list2.recursiveReverse()
list2.printList()
