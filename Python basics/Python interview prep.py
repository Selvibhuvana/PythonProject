
# finding duplicates in a list
data = [1,2,2,3,4,5,5,6,7,7]

duplicates = []
for i in data:
    if data.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)

# finding intersection between 2 lists

data = [1,2,2,3,4,5,5,6,7,7]
data1 = [6,7,8,9]

interset = list(set(data) & set(data1))

print(interset)


# finding frequency of elements in a list
data = [1,2,2,3,4,5,5,6,7,7]
freq = {}
for i in data:
    freq[i] = freq.get(i,0)+1

print(freq)

from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)
print(iris.target)


a = ['Selvi','appu','k']
print(a[:])
b = ' '.join(a[:-1])
print(b)




print(time.time())