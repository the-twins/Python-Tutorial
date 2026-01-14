class Dog:
    
    kind = 'canine'
    tricks = []
    
    def __init__(self, name):
        self.name = name
        
if __name__ == '__main__':
    d = Dog('Fido')
    e = Dog('Buddy')
    print(d.kind)
    print(e.kind)
    print(d.name)
    print(e.name)
    
    d.kind = 'canis'
    print(d.kind)
    print(e.kind)
    
    Dog.kind = 'canis'
    print(d.kind)
    print(e.kind)
    
    print(d.tricks)
    print(e.tricks)
    d.tricks.append('roll over')
    e.tricks.append('play dead')
    print(d.tricks)
    print(e.tricks)
    
    d.tricks = ['roll over']
    e.tricks = ['play dead']
    print(d.tricks)
    print(e.tricks)
    