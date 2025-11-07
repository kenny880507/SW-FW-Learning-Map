class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        new_node = Doubly_Linked_List_Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        new_node = Doubly_Linked_List_Node(x)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        if self.head is not None:
            x = self.head.item
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
        
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        if self.tail is not None:
            x = self.tail.item
            self.tail = self.tail.prev
            if self.tail is None:
                self.head = None
            else:
                self.tail.next = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        
        if x1 is self.head:
            self.head = x2.next
        else:
            x1.prev.next = x2.next
        if x2 is self.tail:
            self.tail = x1.prev
        else:
            x2.next.prev = x1.prev
        L2.head = x1
        x1.prev = None
        L2.tail = x2
        x2.next = None
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        if L2.head is None:
            return
        
        xn = x.next
        x1 = L2.head
        x2 = L2.tail
        
        x.next = x1
        x1.prev = x
        
        xn.prev = x2
        x2.next = xn
        
        L2.head = None
        L2.tail = None
        pass
