# slow/ fast pointer technique to find the middle

class node:
    def __init__(self, label):
        self.label = label
        self.next = None
    
def appendNode(head, label):
    while head.next is not None:
        head = head.next
    print(head.label, "->", end=" ")
    newNode = node(label)
    head.next = newNode

head = node("A")
nodeLabels = ["B", "c", "D", "E"]
for label in nodeLabels:
    appendNode(head, label)
