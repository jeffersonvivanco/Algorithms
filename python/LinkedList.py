class Node():
    def __init__(self, number, next = None):
        self.number = number
        self.next = next
    def _set_next_(self, next):
        self.next = next
    def _set_data_(self, data):
        self.data = data
    def _print_node_(self):
        if self.next:
            return 'Node number: ' + str(self. number) + ' , number of next element: ' + str(self.next.number)
        else:
            return 'Node number: ' + str(self. number) + ' , number of next element: None' 

class LinkedList():
    def __init__(self, node):
        self.head = node
        self.next = None

    def _add_node(self, node):
        temp = self.head
        while not temp.next is None:
            temp = temp.next
        temp.next = node

    def _delete_node(self, key):
        temp = self.head
        if temp is None:
            return None
        while not temp.number is key and not temp.next is None:
            follower = temp
            temp = temp.next
        if not temp.number is key:
            return None
        if temp.number is key and temp is self.head:
            deleted_number = temp.number
            self.head = temp.next
            return deleted_number
        if temp.number is key and not temp is self.head:
            deleted_number = temp.number
            follower.next = temp.next
            return deleted_number
        return None
    # delete node recursive method  
    def _delete_node_rec(self, key):
        if self.head is None:
            return None
        else:
            self.head = self._delete_node_rec_helper(self.head, key)
                    
    def _delete_node_rec_helper(self, L, key):
        if L is None:
            return None
        if L.number is key:
            return L.next
        else:
            L._set_next_(self._delete_node_rec_helper(L.next, key))
            return L

    def _print_list_(self):
        temp = self.head
        str_rep = str(temp.number)
        while not temp.next is None:
            temp = temp.next
            str_rep += ' -> ' + str(temp.number)
        return str_rep



head = LinkedList(Node(1))
head._add_node(Node(2))
head._add_node(Node(3))
head._add_node(Node(4))
head._add_node(Node(5))
head._add_node(Node(6))
head._add_node(Node(7))
head._delete_node_rec(1)
print('Deleting number ' + str(1))
print(head._print_list_())

