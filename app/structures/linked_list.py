from typing import Optional
import json

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next : Optional['ListNode'] = None
    
class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None

    def insert(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find(self, predicate) -> Optional[ListNode]:
        current = self.head
        while current:
            if predicate(current.data):
                return current.data
            current = current.next
        return None
    
    def delete(self, predicate):
        if self.head is None:
            return None
        
        if predicate(self.head.data):
            deleted = self.head
            self.head = self.head.next
            return deleted

        current = self.head
        while current.next:
            if predicate(current.next.data):
                deleted = current.next
                current.next = current.next.next
                return deleted
            current = current.next
        return None
    
    def list_items(self):
        list = []
        currentNode = self.head
        while(currentNode is not None):
            list.append(currentNode.data)
            currentNode = currentNode.next
        return list