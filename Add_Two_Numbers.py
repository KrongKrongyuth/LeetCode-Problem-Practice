# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def __init__(self) : self.head = None

    def addTwoNumbers(self, l1, l2):
        value_from_l1, value_from_l2, counter_l1, counter_l2, i = "", "", 0, 0, 0

        while True :
            if l1.next != None : value_from_l1 += str(l1.val); l1 = l1.next
            elif counter_l1 == 0 : value_from_l1 += str(l1.val); counter_l1 += 1

            if l2.next != None : value_from_l2 += str(l2.val); l2 = l2.next
            elif counter_l2 == 0 : value_from_l2 += str(l2.val); counter_l2 += 1

            if counter_l1 != 0 and counter_l2 != 0 : break

        result = int(value_from_l1[::-1]) + int(value_from_l2[::-1])
        result = str(result)[::-1]

        while i < len(result) :
            pointer = self.head
            if pointer == None : self.head = ListNode(result[i])
            else :
                while True :
                    if pointer.next == None :
                        pointer.next = ListNode(result[i])
                        break
                    pointer = pointer.next
            i += 1

        return self.head