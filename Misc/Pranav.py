'''
Program to perform constant time deletion in a linked list
Author: Mantha Sai Gopal
Reg.no: 23358
'''

class Node(object):
    def __init__(self, value:int):
        self.value = value
        self.next = None

class LinkedList(object):
    #When the list is initialised we have a head which points to the first node 
    #The list could be empty once initialised so we by default give head a 'None'
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def append(self, new_element:int):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = Node(new_element)
        else:
            self.head = Node(new_element)
        self.length += 1

    def get_position(self, position: int)    -> int:
        if position < 0 or position >= self.length:
            print("Invalid position")
            return None

        counter = 0
        current = self.head

        while current:
            if counter == position:
                return current
            else:
                current = current.next
                counter += 1

        print("Position exceeding length of linked list")
        return None

    def insert(self, new_element:int, position:int):
        if position < 1 or position > self.length + 1:
            print("Invalid position")
            return
        
        counter = 1
        current = self.head
        if position == 1:
            new_element.next = self.head.next
            self.head = new_element
        else:
            if self.length >= position :
                while current:
                    if counter == position-1:
                        new_element.next = current.next
                        current.next = new_element
                        break
                    else:
                        current = current.next
                        counter += 1
        self.length += 1

    def delete(self, value):
        if not self.head :
            return None
        current = self.head
        if current.value == value:
            self.head = current.next
            self.length -= 1
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    self.length -= 1
                    break
                current = current.next

    def getPtr(self, position: int):
        if position < 0 or position >= self.length or not self.head:
            print("Invalid position")
            return None

        counter = 0
        current = self.head

        while current:
            if counter == position:
                return id(current)
            current = current.next
            counter += 1

    def delPtrElement(self, pointer):
        if self.length == 0 or not self.head:
            print("Empty Linked List ... Invalid operation !!!")
            return

        # Check if the node to delete is the last node (no "next" node)
        if not pointer.next:
            print("Inserting -∞ at the last node...")
            pointer.value = float("-inf")
            self.length -= 1
            return

        # Copy the value from the next node to the current node
        pointer.value = pointer.next.value

        # Bypass the next node to complete the deletion
        pointer.next = pointer.next.next

        self.length -= 1

    def insertPointer(self,pointer:Node,newElement : int):

        if not pointer:
            print("Invalid Pointer location")
            return

        newNode = Node(newElement)
        newNode.next=pointer.next
        pointer.next = newNode
        self.length += 1

    def printLinkedList(self):
        current = self.head
        while current:
            next_node = current.next
            if next_node:
                arrow = " --> "
            else:
                arrow = " --> None"
            print(f"{current.value}{arrow}",end='')
            current = next_node
        print('\n')

    def len(self):
        return self.length  

ll1 = LinkedList()
for i in range(10):
    ll1.append(i)

ll1.printLinkedList()
print("Lenght-{}\n".format(ll1.len()))

#Use index for deletion not the position value 
ptr1 = ll1.get_position(5)

ll1.insertPointer(ptr1,777)
ll1.printLinkedList()
print("Lenght-{}\n".format(ll1.len()))

ll1.delPtrElement(ptr1)
ll1.printLinkedList()
print("Lenght-{}\n".format(ll1.len()))

ptr2 = ll1.get_position(9)
ll1.delPtrElement(ptr2)
ll1.printLinkedList()
print("Lenght-{}\n".format(ll1.len()))