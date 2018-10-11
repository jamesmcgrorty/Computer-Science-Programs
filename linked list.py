class LinkedList:
    def __init__(self):
        self.length = 0
        self.sp = -1
        self.lp = -1

    def insert(self, data):
        try:
            current = self.sp
            inserted = False
            if current == -1:
                self.sp = Node(data, -1)
                self.lp = self.sp
                self.length = 1
            else: 
                while current != -1 and not inserted:
                    if data <= current.data and current == self.sp:
                        self.sp = Node(data, current)
                        inserted = True
                    elif data >= current.data and current == self.lp:
                        current.pointer = Node(data, -1)
                        self.lp = current.pointer
                        inserted = True
                    elif data >= current.data and data <= current.pointer.data:
                        current.pointer = Node(data, current.pointer)
                        inserted = True
                    else:
                        current = current.pointer
            if inserted:
                self.length = self.length + 1
        except:
            print("You may have used different data types.  Don't be so stupid next time")

    def print(self):
        current = self.sp
        while current != -1:
            print(current.data)
            current = current.pointer

class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

