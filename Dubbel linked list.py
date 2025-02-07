class Dubbel:
    def __init__(self,data):
        self.pre = None
        self.data = data
        self.next = None

class MDubbel:
    def __init__(self):
        self.head = None

    def insert_head(self,data):
        new_node = Dubbel(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        new_node.next = current
        current.pre = new_node
        self.head = new_node

    def insert_end(self,data):
        new_node = Dubbel(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current:
            if current.next is None:
                current.next = new_node
                new_node.pre = current
                return
            current = current.next

    def insert_mid(self,data,t):
        new_node = Dubbel(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current:
            if current.data == t:
                after = current.next
                current.next = new_node
                new_node.pre = current
                new_node.next = after
                after.pre = new_node
            current = current.next


    def travers_down(self):
        current = self.head
        while current:
            print(f"data : {current.data}     previous value : {current.pre}     next value : {current.next}")
            current = current.next


    def delete_head(self):
        if self.head is None:
            print("no elements in the list")
            return

        current = self.head
        after = current.next
        current.next = None
        after.pre = None
        self.head = after


    def delete_end(self):
        if self.head is None:
            print("no elements in the list")
            return

        current = self.head
        while current:
            if current.next is None:
                before = current.pre
                current.pre = None
                before.next = None
            current = current.next

    def delete_mid(self,t):
        if self.head is None:
            print("no elements in the list")
            return

        current = self.head
        while current:
            if current.data == t:
                before = current.pre
                after = current.next

                before.next = after
                after.pre = before
            current = current.next

    def search(self,t):
        if self.head is None:
            print("no elements in the list")
            return

        current = self.head
        while current:
            if current.data is t:
                print(f"data : {current.data}     next : {current.next}     previous : {current.pre}")
                return
            current = current.next

    def travers_up(self):
        current = self.head
        while current:
            if current.next is None:
                break
            current = current.next

        while current:
            print(f"data : {current.data}     previous value : {current.pre}     next value : {current.next}")
            current = current.pre


list1 = MDubbel()



# insertion at the head
list1.insert_head(3)
list1.insert_head(2)
list1.insert_head(1)
list1.travers_down()
print(1000*"=")



# insertion at the end
list1.insert_end(97)
list1.insert_end(98)
list1.insert_end(99)
list1.insert_end(100)
list1.travers_down()
print(1000*"=")



# insertion at a specific location
list1.insert_mid(48,3)
list1.insert_mid(49,48)
list1.insert_mid(50,49)
list1.insert_mid(51,50)
list1.insert_mid(52,51)
list1.travers_down()
print(1000*"=")



# deletion at the head
list1.delete_head()
list1.delete_head()
list1.travers_down()
print(1000*"=")



# deletion at the end
list1.delete_end()
list1.delete_end()
list1.travers_down()
print(1000*"=")



# deletion at a specific location
list1.delete_mid(50)
list1.delete_mid(49)
list1.travers_down()
print(1000*"=")



# searching for a single item in the list
list1.search(51)
list1.search(48)
print(1000*"=")


# traversing using the previous value
list1.travers_up()
print(1000*"=")
