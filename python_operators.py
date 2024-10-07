a = 11
b = 5
result = a < 6
type_a = type(result) # type() returns the data type of the value
print(f"result =  {result} and its data type is {type_a}")

x = 10
x = 14
print(x) # this will print 14 as its overwrites the previous answer

a = "Hello, I am here"
a = "Please"
print(a) #this will print "Please" as it overwrites the previous answer

m = "This is a text"
m = 23
print(m) # This will print 23 as it overwrites the previous answer

unit_name = "Level 4 Programming" # assign variable
print("This unit is: ", unit_name) # print varible
print("The 1st character is:", unit_name[0]) # Access first character using index 0
print("The 4th character is:", unit_name[3]) # 4th character is of index 4 - 1 = 3
print("The 9th character is:", unit_name[8]) # 9th character is of index 9 - 1 = 8

greeting_string = "Welcome to Programming unit! This is level 4 unit :)"
print(greeting_string) # print whole string
print(greeting_string[0], greeting_string[4]) # print the 1st and 5th character
print(greeting_string[0:5]) # prints the first 5 characters
print(greeting_string[-1]) # prints the last character
print(greeting_string[-4:]) # prints the last 4 characters


'''
greeting_string[0] = "X" # Strings do not support item assinment
print(greeting_string)

'''

a = 11.0
print(type(a)) # Float data type

a = "11"
print(type(a)) # String data type

a = "11" + "11"
print(type(a)) # String data type

a = "a"
print(type(a)) # String data type

a = True
print(type(a)) # Boolean data type

a = False
print(type(a)) # Boolean data type

x = 10.5
print(type(x))

x = int(x) # removes decimal point value

text_strip = "     Yo dawg  " # removes trailing spaces
print(text_strip.strip())

text_split = "Yo dawg" # splits string into individual words
print(text_split.split())

text_count = "Yo dawg whats up" # counts each a value in the string
print(text_count.count("a"))