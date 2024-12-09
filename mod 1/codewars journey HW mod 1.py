# create a function that takes an integer as an argument and returns even and odd 
num = 10   # input number that will get defined as even or odd

if num % 2 == 0:
    print(f"{num} is even")  #solution for the even output
else:
    print(f"{num} is odd")    # solution for the odd output 
    
#output
10 is even


#transforming integers into strings 
numbers = "12345"
print(type(numbers))
integers = int(numbers)
print(integers)
print(type(integers))

#output
<class 'str'>
12345
<class 'int'>

#return the number count of vowels in the given string being "a,e,i,o,u"

def getCount(sentence):
    vowels = 'aeiou'

vowels_count = 0 
for char in sentence: 
    if char.lower() in vowels:
        vowels_count += 1
return vowels_count



