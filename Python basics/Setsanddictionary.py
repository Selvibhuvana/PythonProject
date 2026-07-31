"""
#fruits = ['apple', 'banana', 'apple','orange'] # this is list
f1 = {'apple', 'banana', 'apple','orange'} # this is set
f2 = {'apple', 'guava', 'peach','orange'}

#print (fruits)
#print (fruits1)
f1.add("peach")
print(f1)
f3 = f1.union(f2)
print(f3)
f3 = f1.intersection(f2)
print(f3)

#converting list to set
data1 = [6,7,8,9]
set1 = set(data1)
print (set1)
"""
# Dictionary - Key value pair

dict = {1:"selvi",2:"Appu",3:"Lakshi",4:"Krithi"}
print(dict[3])
dict[5] = "Dhivi"
print(dict)

print(4 in dict) # returns true or false based on the key is in dictionary

people = {"selvi":33,"Appu":32 ,"Lakshi" : 21 , "Krithi" : 23 , "Dhivi" : 15}
print(people.items())

age_thresh = 30
#above_thresh = [(name,age) for name, age in people.items() if age >age_thresh]
#print (above_thresh)

above_thresh = []
for name, age in people.items():
    if age > age_thresh:
        above_thresh.append(people[name])

print (above_thresh)

# Differentiating emp,ty set and dict

l=[]
t=()
s=set()
d={}
print(type(l))
print(type(t))
print(type(s))
print(type(d))


#adding subdictionary into a main dictionary

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome','population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)



