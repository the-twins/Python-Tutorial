class MyClass:
    def __init__(self, a1: int, a2: int):
        self.a1 = a1
        self.a2 = a2
        
    def sum(self):
        return self.a1 + self.a2
        
        
if __name__ == '__main__':
    x = MyClass(2, 3)
    
    x.a3 = 5
    print(x.a1, x.a2, x.a3)
    print(x.sum())
    del x.a3
    
    x.a1 = 20
    x.a2 = 30
    xs = x.sum
    for i in range(10):
        print(xs())
        