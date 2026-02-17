def quote(f):
    def wrapper(*args, **kwargs):
        result = '"' + f(*args, **kwargs) + '"'
        return result
    return wrapper
    

def citation(opening, closing):
    def decorator(f):
        def wrapper(*args, **kwargs):
            result = opening + f(*args, **kwargs) + closing
            return result
        return wrapper
    return decorator
 
 
def upper_1(st: str) -> str:
    return st.upper()
   

@quote
def upper_2(st: str) -> str:
    return st.upper()
    

@citation('<<', '>>') 
def upper_3(st: str) -> str:
    return st.upper()
    
     
if __name__ == '__main__':
    print(upper_1('Hello'))
    
    quoted = quote(upper_1)
    print(quoted('Hello'))
    
    print(upper_2('Hello world'))
    
    decorator = citation('<<', '>>')
    cited = decorator(upper_1)
    print(cited('Bye'))
    
    print(upper_3('Good'))
    