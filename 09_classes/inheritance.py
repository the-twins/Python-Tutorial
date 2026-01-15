class Person:
    
    def __init__(self, name: str, born: int):
        self.name = name
        self.born = born
        
    def introduce(self):
        print(f'Hello! I am {self.name}. I was born in {self.born}.')


class Programmer(Person):
    
    def __init__(self, name: str, born: int, language: str):
        Person.__init__(self, name, born)
        self.language = language
        
    def favorite_language(self):
        print(f'My favorite language is {self.language}.')
        
        
class Philosopher(Person):
    
    def __init__(self, name: str, born: int, philosophy: str):
        Person.__init__(self, name, born)
        self.philosophy = philosophy
        
    def favorite_philosophy(self):
        print(f'My philosophy is {self.philosophy}.')
        
        
#alternative option without inheritance        
class Doctor:
    
    def __init__(self, name: str, born: int, specialization: str):
        self.person = Person(name, born)
        self.specialization = specialization

    def favorite_specialization(self):
        print(f'I am {self.specialization}.')  
        
        
if __name__ == '__main__':
    adam = Person('Adam', -4000)
    adam.introduce()
    guido = Programmer('Guido', 1956, 'Python')
    guido.introduce()
    guido.favorite_language()
    hegel = Philosopher('Georg Wilhelm Friedrich Hegel', 1770, 'idealism')
    hegel.introduce()
    hegel. favorite_philosophy()
    popov = Doctor('Popov', 1867, 'therapist')
    popov.person.introduce()
    popov.favorite_specialization()
    