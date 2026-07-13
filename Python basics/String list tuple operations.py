"""
#STRING Operations
str = 'Hi I am in Canada'

print(len(str))
print(str[0:3])
print(str[:3:1]) # 3rd character inside [] is escape characters 1 is default
#in 1st character in [] even if 0 is not mentioned it means 0 --> the 1st character in the string
print(str[:3:2]) # in this case it will escape 2 characters
print(str[:17:2]) # in this case it will escape 2 characters for the entire string
print(str[::-1]) # reversal of string - the first 2 colons are start and stop and 3rd one is step so that the string is preinted from reverse

print(str[11:18]) # the boundary values are not considered , characters between them are displayed


#LISTS Operations

fruits = ['apple', 'banana', 'orange']
fruits.append('mango')
print(fruits)
fruits.insert(1, 'Peach')
print(fruits)
print(fruits[2])
#fruits.pop(3)
fruits.remove('Peach') # or fruits.remove(fruits[2])
print(fruits)
fruits.sort()
print(fruits)
print(fruits.count('Peach'))
print(fruits.index('orange'))



fruits = ['apple', 'banana', 'orange']
print (len(fruits))
fruits = ('apple', 'banana', 'orange')
print (len(fruits))
print(fruits[2])

str = "etlqalabs"
print(str[::-1])
"""

fruits = ['apple', 'banana', 'orange','Peach','guava']
print (fruits[0])
print (fruits[-1])

str = 'Hi I am in Canada'
print(str[12:16])
print(str[11:])
print(str[:17])

#negative indexing
print (str[-6:])

#list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
print (house[4][1])


# Delete and + operation

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[-4:-2]
# Print the updated list
print (areas)
#to add
areas = areas+["poolhouse", 24.5]
print (areas)

#Change the second command, that creates the variable areas_copy, such that areas_copy is an explicit copy of areas.
# After your edit, changes made to areas_copy shouldn't affect areas.
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)  # when we do list() copy of the list the actual list is not impacted
#areas_copy = areas # this command will modify both list even if changes are made in one

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
print(areas_copy)


#strings more actions

print("she is good")
print ("It's her book")
print("she says \"Hello world\"")  #escape the additional double quotes using \
print('she says "Hello world"')  #or use single quotes

my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

name = 'John Doe'
age = 26
city = ('Ottawa')

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string
name_and_age += city

print(name_and_age)

# String interpolation
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

std1 = 'Alice'
std2 = 'Nanno'
Marks_together = 250
print(f'The marks of {std1} and {std2} is {Marks_together}')


# string methods
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world

my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']


my_list = ['hello', 'world']

joined_str = '!'.join(my_list)    # the one before dot is seperator to join
print(joined_str)

my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

my_str = 'hello world'

world_index = my_str.find('hello')
print(world_index)  # 6

my_str = 'hello world'

o_count = my_str.count('w')
print(o_count)  # 2

my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)

my_str = 'hello world'

capitalized_my_str = my_str.title()
print(capitalized_my_str)

str = " I like to go on hikes with my dog.  "
clean = str.strip()
print (str)
print (clean)

str = 'catastrophe'
print (str[:-2:2])  #ctsrp
print (str[1:-1:2])

colors = """red,
orange,
green,
purple,
yellow"""

print (colors.split(',\n'))
print (colors.split(',\t'))
print (colors.split(','))

str = 'catastrophe'
for x in str:
    print (x)

str = 'Hello'
for index,x in enumerate(str):
    print(index, ": " ,x)

str = 'Happy'
seperator = 'Un'
new = seperator.join(str)
print (new)


def adjective_to_verb(sentence,index):
    return sentence.split()[index].rstrip(".") + 'en'

"""    newsentence = sentence.replace('.','')
    splitlist = newsentence.split()
    return splitlist[index]+'en'
"""


print(adjective_to_verb('I need to make that bright.', -1 ))

worlist = adjective_to_verb('I need to make that bright.') #, -1 )
print (worlist)


def remove_suffix_ness(word):
    if word[-1:-6] == 'iness':
        return word.replace('iness','y')
    return word.replace('ness','')

print(remove_suffix_ness("heaviness"))


word = 'happiness'
print (word[-5:])

