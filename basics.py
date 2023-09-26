import math

print('new')
# year=input('enter year')
year=2000
print(2023-int(year))
strs="this is a string"

#copy strings
print([strs[3:]])
print([strs[:3]])
copy_strs=strs[:]
print("copied string "+ copy_strs)


#formatted strings
formated_string=f'original string is {strs} and copied is {copy_strs}'
print("formatted string " + formated_string)
print(formated_string.upper())


#find, replace and in
print("string" in formated_string)
print(strs.find("is"))
print(strs.find("I")) #gives -1 if char/string not present in string
print(strs.replace("string","copied string"))

#length
print("length of "+ strs + " is " + str(len(strs)))


#divide
print(10/3)
print(10//3)


#power
print(10**3)

#operator precedence
# parenthesis> exponentation(power) > multiply/divide > add/substract


#other built in functions
x=2.9
print(round(x))
print(abs(-2.9))

print(math.ceil(2.9))

#if statements
if(True):
    print("if statement")
else:
    print("false")

x=30
if(x==10):
    print("x is 10")
elif(x==30):
    print("x is 30")
else:
    print("x is unknown")

#and or not
if(x==30 and True):
    print("and statement")

if(not(x==35)):
    print("not statement")

if(x==34 or True):
    print("or statement")


#while loop
# secret=9
# guess_count=0
# guess_limit=3
# while(guess_count!=guess_limit):
#              guess = int(input("your guess?"))
#              guess_count += 1
#              if guess==secret:
#                  print("win")
#                  break
#
#
# else:
#                  print("lost chances")



#for loop
for item in "aman":
    print(item)
for item in ["aman","is", "coder"]:
    print(item)
for item in range(10):
    print(item)

print("table of 2 with skip in range")
for item in range(2,12,2):
    print(item)

for i in range(1, 5):
    print('f' * i)


# -ve index access
ary = ["a", "b", "v", "d"]# this is a list
print(ary[-1])
ary[0]="aman"
print(ary)


# 2d list
matrix=[
    [1,2,3],
    [4,5,6]
]

for row in matrix:
    for item in row:
        print(item)

#operations on list
numbers=[5,7,2,4,5]
numbers.append(3)

print(numbers)
numbers.insert(1,100);#1is index, 100 is value
print(numbers)
numbers.remove(100)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(7))
# print(numbers.index(100)) #gives error
print(100 in numbers)


print(numbers.count(5) )

print(numbers.sort()) # empty result


print(numbers)  # now gives sorted string

numbers.reverse() # descending order

numbers2=numbers.copy()
# a change in numbers do not affect its copy number2

numbers.clear()
print(numbers)

#tuple: like a list but cannot be modified

tpl= (1,2,3)

#cannot add or remove items for tuple

print(tpl[1])

#tpl[1]=0 gives error because they cant be modified


#unpacking:
#works for both list and tuple

coordinates=(1,2,3)

x, y, z = coordinates
print(x)

#2 hour 18 minutes programming with mosh 6 hour video