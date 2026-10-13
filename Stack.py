class EmptyStackError(Exception):
    pass


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise EmptyStackError("Empty Stack")
        else:
            remove_item = self.items.pop(-1)
            return (remove_item)

    def peek(self):
        if not self.items:
            raise EmptyStackError("Empty Stack")
        else:
            return self.items[-1]
        
    def is_empty(self):
        if not self.items:
            return True
        return False

    def size(self):
        return len(self.items)


            
s = Stack()
s.pop()