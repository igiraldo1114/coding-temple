# variables 

name = "Isabel"
age = 24
height = 5.5

# data types 
age = 24 #integer
height = 5.5 #float 
name = "Isabel" # string 
is_student = True #Boolean

#operations
result = 10 + 5 
comparison = 5>3

#input/output 
name = input("what is your name?")
print(f"hello, {name}!")

name = "Christian"
age = 99
favorite_color = "purple"

#introduction
if condition:
    # code block
elif condition:
    #code block
else:
    #code block
#example
age = int(input("enter your age:"))

if age > = 18:
    print("you are an adult")
else:
    print("you are a minor")
    
#nested if statements and multiple conditions/ introduce and/or logical operators 
age = int(input("enter your age"))
    print("you are a child.")
elif age > = 13 and age < 20:
    print("you are a teenager")
else:
    print("you are an adult")

#final challenge 

exam_score = int (input("input your score"))

if (exam_score > 90):
    print("excellent")
elif (exam_score < 90 and exam_score > 70):
    print("good")
else:
    print("needs improvement")