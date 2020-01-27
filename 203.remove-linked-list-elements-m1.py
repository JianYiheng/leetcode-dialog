from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ptr_head: ListNode = ListNode(0)
        ptr_head.next = head
        ptr_prev = ptr_head
        ptr_curr = ptr_head
        while ptr_curr:
            if ptr_curr.val == val:
                ptr_curr = ptr_curr.next
                ptr_prev.next = ptr_curr
            else:
                ptr_prev = ptr_curr
                ptr_curr = ptr_curr.next
                ptr_prev.next = ptr_curr
        return ptr_head.next


def list2listnode(input_list: List) -> ListNode:
    head = ListNode(input_list[0])
    head.next = None
    if len(input_list) == 1:
        return head
    prev = head
    curr = head
    for i in input_list[1:]:
        curr = ListNode(i)
        prev.next = curr
        prev = curr
    curr.next = None
    return head


def listnode2list(input_head: ListNode) -> List:
    output_list = []
    ptr: ListNode = input_head
    while ptr is not None:
        output_list.append(ptr.val)
        ptr = ptr.next
    return output_list


if __name__ == '__main__':
    input_list = [1]
    ret = Solution().removeElements(list2listnode(input_list), 1)
    print(listnode2list(ret))
