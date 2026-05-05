class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Length calculate karein aur last node tak pahunchein
        last_node = head
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1
        
        # 2. k ko normalize karein (agar k > length ho)
        k = k % length
        if k == 0:
            return head
        
        # 3. List ko circular banayein
        last_node.next = head
        
        # 4. New tail tak pahunchein (length - k - 1 steps from head)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # 5. Break the circle aur naya head set karein
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head