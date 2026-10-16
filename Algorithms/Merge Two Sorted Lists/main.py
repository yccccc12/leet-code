from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        sorted_list = []
        
        while list1 is not None:
            sorted_list.append(list1.val)
            list1 = list1.next

        while list2 is not None:
            sorted_list.append(list2.val)
            list2 = list2.next

        sorted_list.sort()

        dummy = ListNode(-1)
        current = dummy
        for value in sorted_list:
            current.next = ListNode(value)
            current = current.next

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    output = solution.mergeTwoLists(list1, list2)


    

    