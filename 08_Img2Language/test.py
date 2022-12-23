# python test.py


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        # print(type(head))
        while head:
            next = head.next
            print("next : ", next)
            head.next = prev
            prev = head
            head = next
            # print("prev : ",prev)
            # print("head : ", head)
        return prev


head = [1, 2, 3, 4, 5]
obj = Solution()
print(obj.reverseList(head))
