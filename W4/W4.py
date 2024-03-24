# Traverse the linked list
def traverse(head):
    ptr = head
    while True:
        print("The color of the car is {}.".format(ptr.color))
        if ptr.next == head:
            break
        ptr = ptr.next
    print("Finish traverse")

# 需自訂一個類別 (class)
class car: 

    def __init__(self, color):
        self.color = color
        self.next = None

# """
# Initiate the first element of the linked list.
head = car("red") # Add new element.
ptr = head # Set the position of the pointer.
ptr.next = None # There is no next element now.

# Add next element into the linked list.
new_data = car("blue") # Add new element.
ptr.next = new_data
new_data.next = head
ptr = new_data

new = car("black")
new.next = head

ptr = head
while ptr.next != head:
    ptr = ptr.next
ptr.next = new
head = new  
"""
head = car("black")
red = car("red")
pink = car("pink")
blue = car("blue")
ptr = head
ptr.next = red
ptr=ptr.next
ptr.next = pink
ptr=ptr.next
ptr.next = blue
ptr=ptr.next
ptr.next = head

ptr = head
while ptr.next != head:
    ptr = ptr.next
"""
# """
new = car("pink")

ptr = head
while ptr.color != "red":
    ptr = ptr.next

new.next = ptr.next
ptr.next = new

# x.next = I.next
# I.next = x
# """
# """
# find the element which points to head
ptr = head
while ptr.next != head:
    ptr = ptr.next
head = head.next # set the new head(The original second node)
ptr.next = head # point to the new head
# """
# 刪除環狀串列的中間節點
ptr = head 
while ptr.next.color != "pink":
    ptr = ptr.next
ptr.next = ptr.next.next

traverse(head)