class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def print_list(self):
        current = self.head
        elements = []
        
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements) if elements else "The list is empty")
    
    def delete_nth_node(self, n):
        if self.head is None:
            raise ValueError("Cannot delete from an empty list")
        
        if n < 1:
            raise ValueError("Index must be a positive integer")
        
        if n == 1:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        count = 1
        
        while current is not None and count < n:
            prev = current
            current = current.next
            count += 1
        
        if current is None:
            raise ValueError(f"Index {n} is out of range for the list")
        
        prev.next = current.next
    
    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

if __name__ == "__main__":
    print("Creating a new linked list...")
    ll = LinkedList()
    
    print("\nAdding nodes with values 10, 20, 30, 40, 50...")
    for value in [10, 20, 30, 40, 50]:
        ll.add_node(value)
    
    print("\nCurrent list:")
    ll.print_list()  
    
    print("\nDeleting the 3rd node (value 30)...")
    ll.delete_nth_node(3)
    ll.print_list()
    
    print("\nDeleting the 1st node (value 10)...")
    ll.delete_nth_node(1)
    ll.print_list()  
    
    print("\nAttempting to delete the 5th node (out of range)...")
    try:
        ll.delete_nth_node(5)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nAttempting to delete from an empty list...")
    empty_list = LinkedList()
    try:
        empty_list.delete_nth_node(1)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\nFinal list:")
    ll.print_list()  
    print(f"List length: {len(ll)}")  