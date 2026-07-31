import pandas as pd

dict = {
"country":["Brazil", "Russia", "India", "China", "South Africa"],
"capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
"area":[8.516, 17.10, 3.286, 9.597, 1.221],
"population":[200.4, 143.5, 1252, 1357, 52.98] }

df = pd.DataFrame(dict)
#df.set_index("country", inplace=True)
df.index = ["BR","RU","IN","CH","SA"]
print(df)
print(df.loc[["BR","RU"],["area"]])

print(df.iloc[1,3])
print(df.iloc[[1,3]])
print(df.iloc[[1],[3]])


#print(type(df[['country']]))