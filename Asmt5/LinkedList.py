class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return
        else:
            new.next = self.head
            self.head = new

    def insert_at_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new

    def print_ll(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def length_of_ll(self):
        count = 0
        if self.head is None:
            return count
        else:
            current_node = self.head
            while current_node:
                count += 1
                current_node = current_node.next
            return count

    def pop(self):
        if self.head is None:
            return
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None

    def get_position(self, location):
        if location < 0 or location >= self.length_of_ll():
            print("Invalid location")
            return None
        counter = 0
        current_node = self.head
        while current_node:
            if counter == location:
                return current_node
            else:
                current_node = current_node.next
                counter += 1
        return None

    def delete(self, pointer):  # delete in constant time
        # last node case
        if not pointer.next:
            pointer.data = float("-inf")
            return

        # Copy the value from the next node to the current node
        pointer.data = pointer.next.data

        # Bypass the next node to complete the deletion
        pointer.next = pointer.next.next

    def insert(self, location, data):  # insert in constant time
        if not location:
            print("Invalid Pointer location")
            return
        new = Node(data)
        new.next = location.next
        location.next = new


ll = LinkedList()
for i in range(5):
    ll.insert_at_end(i)
ll.print_ll()

print("Let us insert a new node in location 1!")
print("List after the node in location 1 is inserted!")
ptr = ll.get_position(1)
ll.insert(ptr, 121)
ll.print_ll()

ll.delete(ptr)
print("After deleting the node in location 1: ")
print("List after the node in location 1 is deleted!")
ll.print_ll()
