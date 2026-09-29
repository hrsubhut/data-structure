class Solution(object):
    def mergeTwoLists(self, list1, list2):
        arr = []

        while list1:
            arr.append(list1.val)
            list1 = list1.next

        while list2:
            arr.append(list2.val)
            list2 = list2.next

        arr.sort()

        new_head = None
        tail = None

        for x in arr:
            new_node = ListNode(x)

            if new_head is None:
                new_head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        return new_head