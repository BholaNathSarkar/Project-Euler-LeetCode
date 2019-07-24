# Problem: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#          An input string is valid if:
#            - Open brackets are closed by the same type of brackets.
#            - Open brackets are closed in the correct order.
#            - Note that an empty string is also considered valid.

#Approach: steps : 1. Scan form left to right
#                  2.If opening symbol, then add it to a stack.
#                  3.If closing symbol ,then remove the last opening symbol from the stack.
#                  4.If we get an empty stack at last, then we can saythe string contains valid parenthesis.

class Solution:
    def isValid(self, s):
        open_symbol=["[","{","("]
        close_symbol=["]","}",")"]
        stack=[]

        for i in s:
            if i in open_symbol:
                stack.append(i)
            elif i in close_symbol:
                pos=close_symbol.index(i)
                if(len(stack)>0 and open_symbol[pos]==stack[len(stack)-1]):
                     stack.pop()
                else:
                    return False
        if(len(stack)==0):
            return True
str="[()]{}"
print(str," -> ", Solution().isValid(str))
