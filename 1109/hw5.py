def outer(a,b):
    a**2
    def add(a,b):
        sum=a+b
        return sum
    result= add(a,b)  
    result=result+5
    return result

result = outer(5, 10)
print(result)