# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = list()
        while head != None:
            nodes.append(head)
            head = head.next
        
        length = len(nodes)
        if length > 2:
            mid = length // 2
            for i in range(mid): 
                nodes[i].next = nodes[length - i - 1]      # forward
                nodes[length - i - 1].next = nodes[i + 1]  # backward
                
            nodes[mid].next = None
        

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    last = head
    for i in range(2,5):
        node = ListNode(i)
        last.next = node
        last = node
    sol.reorderList(head)
    
    while head != None:
        print(head.val)
        head = head.next