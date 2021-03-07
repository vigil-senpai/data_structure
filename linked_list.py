# linked list

class node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class linked_list:
    def __init__ (self):
        self.headval = None
        self.tailval = None

    def view(self):
        index = self.headval
        if(index is None):
            return
        while (index != self.tailval):
            print(index.dataval, end = ' ')
            index = index.nextval
        print(self.tailval.dataval)

    # PUSH  #

    def push_head(self, new_data):
        if (self.tailval == None):
            self.headval = self.tailval = node(new_data)
            return

        current = node(new_data)
        current.nextval = self.headval
        self.headval = current

    def push_tail(self, new_data):
        if (self.tailval == None):
            self.headval = self.tailval = node(new_data)
            return

        current = node(new_data)
        self.tailval.nextval = current
        self.tailval = current

    def push_after(self, new_data, target):
        index = self.headval
        current = node(new_data)
        if (self.tailval.dataval == target):
            linked_list.push_tail(self, new_data)
            return
        while (index.nextval is not None):
            if(index.dataval == target):
                current.nextval = index.nextval
                index.nextval = current
                return
            index = index.nextval

    def push_before(self, new_data, target):
        index = self.headval
        current = node(new_data)
        if(self.headval.dataval == target):
            linked_list.push_head(self, new_data)
            return
        while(index.nextval is not None):
            if(index.nextval.dataval == target):
                current.nextval = index.nextval
                index.nextval = current
                return
            index = index.nextval

    # POP   #
    
    def pop_head(self):
        if(self.headval is None):
            self.headval = None
            self.tailval = None
            return
        if(self.headval.nextval is None):
            self.headval = None
            self.tailval = None
            return
        temp = self.headval
        self.headval = self.headval.nextval
        del temp

    def pop_tail(self):
        if(self.headval is None):
            self.headval = None
            self.tailval = None
            return
        if(self.headval.nextval is None):
            self.headval = None
            self.tailval = None
            return
        index = self.headval
        while(index.nextval is not None):
            if(index.nextval == self.tailval):
                temp = self.tailval
                self.tailval = index
                del temp

            index = index.nextval

    def pop_number(self, target):
        if(target == self.headval.dataval):
            linked_list.pop_head(self)
            return
        if(target == self.tailval.dataval):
            linked_list.pop_tail(self)
            return
        index = self.headval
        while(index.nextval is not None):
            if(index.nextval.dataval == target):
                temp = index.nextval
                index.nextval = index.nextval.nextval
                del temp
            index = index.nextval


list1 = linked_list()

linked_list.push_head(list1, 3)
linked_list.push_tail(list1, 7)
linked_list.push_head(list1, 9)
linked_list.pop_number(list1, 9)
linked_list.push_tail(list1, 6)
linked_list.pop_tail(list1)
linked_list.push_after(list1, 4, 3)
linked_list.push_before(list1, 10, 4)
linked_list.push_tail(list1, 1)
linked_list.pop_head(list1)
linked_list.push_head(list1, 2)
linked_list.push_after(list1, 11, 1)
linked_list.push_before(list1, 8, 2)
linked_list.pop_tail(list1)
linked_list.push_tail(list1, 22)

linked_list.view(list1)
