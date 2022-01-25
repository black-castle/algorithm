# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = list()
        while head != None:
            nodes.append(head)
            head = head.next
            
        length = len(nodes)
        
        for i in range(0, length - (length % k), k):
            for j in range(k // 2):
                tmp = nodes[i + j]
                nodes[i + j] = nodes[i + k - 1 - j]
                nodes[i + k - 1 - j] = tmp
                
        for i in range(length - 1):
            nodes[i].next = nodes[i+1]
        nodes[length - 1].next = None
        
        return nodes[0]