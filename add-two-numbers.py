# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sum_linked_list(self, linked_list):
        ll_sum = 0
        ll_index = 0

        while linked_list:
            ll_sum = ll_sum + (linked_list.val * (10 ** ll_index))
            linked_list = linked_list.next
            ll_index = ll_index + 1

        return ll_sum

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_sum = self.sum_linked_list(l1)
        l2_sum = self.sum_linked_list(l2)

        linked_list_sum = l1_sum + l2_sum
        result = ListNode(0)
        current = result

        if linked_list_sum > 0:
            while linked_list_sum > 0:
                x = linked_list_sum % 10
                linked_list_sum = linked_list_sum // 10 
                current.next = ListNode(x)
                current = current.next
        else:
            current.next = ListNode(0)
            current = current.next

        return result.next
