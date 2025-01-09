# with generator 
def square(i):
   for i in range(i):
    i = i**2
    yield i
square(10)
for i in square(10):
    print(i)    

# withput generator
def square(i):
    for i in range(i):
        i =i+2
    return i
res = square(20)
print(res)

     