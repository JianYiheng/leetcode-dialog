from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ptr_head: ListNode = ListNode(0)
        ptr_head.next = head
        ptr_head_new: ListNode = ListNode(0)
        ptr_self: ListNode = ptr_head.next
        ptr_prev: ListNode = ptr_head_new
        ptr_curr: ListNode = None

        while ptr_self:
            ptr_prev = ListNode(ptr_self.val)
            ptr_prev.next = ptr_curr
            ptr_curr = ptr_prev

            ptr_self = ptr_self.next
        ptr_head_new.next = ptr_curr
        return ptr_head_new.next


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
    input_test = []
    ret = Solution().reverseList(list2listnode(input_test))
    print(listnode2list(ret))
