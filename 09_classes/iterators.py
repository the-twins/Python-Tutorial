class ListItem:
    
    def __init__(self, value, next_item = None):
        self.value = value
        self.next = next_item
        
        
class LinkedListIter:
    
    def __init__(self, item):
        self.item = item
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.item:
           raise StopIteration
        temp = self.item
        self.item = self.item.next
        return temp.value
           
    
class LinkedList:
    
    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self, n):
        freash = ListItem(n)
        if not self.first:
            self.first = freash
        else:
            self.last.next = freash
        self.last = freash
        
    def __iter__(self):
        return LinkedListIter(self.first)
                
    def print(self):
        item = self.first
        while item:
            print(item.value, end=' ')
            item = item.next


if __name__ == '__main__':
    i = LinkedList()
    i.add(2)
    i.add(3)
    i.add(4)
    
    i.print()
    print()
    for j in i:
        print(j, end=' ')
      
    it1 = iter(i)
    it2 = iter(i)
    print()
    while True:
        try:
            print(next(it1), end=' ')
        except StopIteration:
            break
    print()
    while True:
        try:
            print(next(it2), end=' ')
        except StopIteration:
            break
