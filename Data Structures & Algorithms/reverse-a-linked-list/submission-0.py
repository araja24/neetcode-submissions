# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            nxt = curr.next
            print("nxt: ", nxt.val if nxt else "None")
            curr.next = prev
            print("curr.next: ", curr.next.val if curr.next else "None")
            
            prev = curr
            print("prev: ", prev.val)
            curr = nxt
            print("curr: ", curr.val if curr else "None")


        return prev




