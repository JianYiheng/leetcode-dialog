from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        prev = None
        cur = head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
    

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
    input_test = [1, 2, 3, 4, 5]
    ret = Solution().reverseList(list2listnode(input_test))
    print(listnode2list(ret))
