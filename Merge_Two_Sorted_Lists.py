# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def __init__(self) :
        self.head = None
    def mergeTwoLists(self, list1, list2):
        condition = (list1 and list2 != None)
        if condition :
            
            # Merging Algorithm #
            pass

        else :
            if list1 != None : return list1
            elif list2 != None : return list2
            else : return ListNode('')