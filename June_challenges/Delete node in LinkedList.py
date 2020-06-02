# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while True:
            pointer = node.next
            node.val = pointer.val
            
            if pointer.next is None:
                node.next = None
                break
                
            node = pointer