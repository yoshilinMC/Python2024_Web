# right traverse
def rTraverse(head):
    print("start right traverse!")
    ptr = head 
    while ptr != None:
        print("The color of the car is {}".format(ptr.color))
        ptr = ptr.next
    print("finish right traverse")
# left traverse
def lTraverse(head):
    print("start left traverse!")
    ptr = head 
    while ptr.next != None:
        ptr = ptr.next
    while ptr != None:
        print("The color of the car is {}".format(ptr.color))
        ptr = ptr.previous
    print("finish leftt traverse")

# 建立雙向串列 自訂類別(car)
class car:
    def __init__(self,color):
        self.color = color
        self.previous = None
        self.next = None

# Intitate the first element of the double link
head = car("red")
ptr = head
ptr.previous = None
ptr.next = None 

# Add next element into linked list 
new = car("blue") # create new object 
ptr.next = new # set the head node previous element 
new.previous = ptr # set the new node previous element
ptr = new

rTraverse(head)
lTraverse(head)