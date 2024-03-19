class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def count(head, key):
    res = 0
    while head:
        if head.data == key:
            res +=1
        head = head.next
    return res