class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
head.next = Node(3)
head.next.next = Node(4)

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next 
        current.next = prev      
        prev = current           
        current = next_node      
    
    return prev 

new_head = reverse_linked_list(head)
print("MY LIST")
link = new_head
while link:
    print(link.value, end=" -> ")
    link = link.next
print("None")         