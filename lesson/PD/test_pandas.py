import pandas as pd

# mydataset = {
#   'sites': ["Google", "Runoob", "Wiki"],
#   'number': [1, 2, 3]
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)

# a = [1, 2, 3]
# myvar = pd.Series(a)
# print(myvar)

# a = ["Google", "Runoob", "Wiki"]
# myvar = pd.Series(a, index=["x", "y", "z"])
# print(myvar)

# sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
# myvar = pd.Series(sites)
# print(myvar)

# sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
# myvar = pd.Series(sites, index=[1, 2])
# print(myvar)

# sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
# myvar = pd.Series(sites, index=[1, 2], name="RUNOOB-Series-TEST")
# print(myvar)

# data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
# df = pd.DataFrame(data, columns=['Site', 'Age'], dtype=object)
# print(df)

data = {'Site': ['Google', 'Runoob', 'Wiki'], 'Age': [10, 12, 13]}
df = pd.DataFrame(data)
print(df)
