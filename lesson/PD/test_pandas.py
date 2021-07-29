import json
import pandas as pd
from glom import glom

# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
# pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)  # 加了这一行那表格的一行就不会分段出现了
# pd.set_option('display.max_colwidth', 1000)
# pd.set_option('display.height', 1000)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2, 3]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)

a = ["Google", "Runoob", "Wiki"]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites)
print(myvar)

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites, index=[1, 2])
print(myvar)
myvar = pd.Series(sites, index=[1, 2], name="RUNOOB-Series-TEST")
print(myvar)

data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
df = pd.DataFrame(data, columns=['Site', 'Age'], dtype=object)
print(df)

data = {'Site': ['Google', 'Runoob', 'Wiki'], 'Age': [10, 12, 13]}
df = pd.DataFrame(data)
print(df)

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
# 返回第0，1行
print(df.loc[[0, 1]])
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)
print(df.loc["day2"])

df = pd.read_csv('nba.csv')
print(df.to_string())
print(df)
print(df.head())
print(df.tail())
print(df.info())

# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
# 字典
dict1 = {'name': nme, 'site': st, 'age': ag}
df = pd.DataFrame(dict1)
# 保存 dataframe
df.to_csv('site.csv')

data = [
    {
        "id": "A001",
        "name": "菜鸟教程",
        "url": "www.runoob.com",
        "likes": 61
    },
    {
        "id": "A002",
        "name": "Google",
        "url": "www.google.com",
        "likes": 124
    },
    {
        "id": "A003",
        "name": "淘宝",
        "url": "www.taobao.com",
        "likes": 45
    }
]
df = pd.read_json('sites.json')
df = pd.DataFrame(data)
print(df.to_string())

# 字典格式的 JSON
s = {
    "col1": {"row1": 1, "row2": 2, "row3": 3},
    "col2": {"row1": "x", "row2": "y", "row3": "z"}
}
# 读取 JSON 转为 DataFrame
df = pd.DataFrame(s)
print(df)

URL = 'https://static.runoob.com/download/sites.json'
df = pd.read_json(URL)
print(df)

df = pd.read_json('nested_list.json')
print(df)

# 使用 Python JSON 模块载入数据
with open('nested_list.json', 'r') as f:
    data = json.loads(f.read())
# 展平数据
df_nested_list = pd.json_normalize(data, record_path=['students'])
df_nested_list = pd.json_normalize(
    data,
    record_path=['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)

# 使用 Python JSON 模块载入数据
with open('nested_mix.json', 'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(
    data,
    record_path=['students'],
    meta=[
        'school_name',
        'class',
        ['info', 'president'],
        ['info', 'address'],
        ['info', 'contacts', 'tel'],
        ['info', 'contacts', 'email']
    ]
)
print(df)

df = pd.read_json('nested_deep.json')
data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)

# 默认NaN n/a 和 NA 当作空数据，na -- 不是空数据
df = pd.read_csv('property-data.csv')
print(df['NUM_BEDROOMS'])
missing_values = ["n/a", "na", "--"]
df = pd.read_csv('property-data.csv', na_values=missing_values)
print(df['NUM_BATH'].isnull())

# 删除包含空数据的行
df = pd.read_csv('property-data.csv')
new_df = df.dropna()
print(new_df.to_string())

# 移除 ST_NUM 列中字段值为空的行
df = pd.read_csv('property-data.csv')
df.dropna(subset=['ST_NUM'], inplace=True)
print(df.to_string())

# 使用 12345 替换空字段
df = pd.read_csv('property-data.csv')
df.fillna(12345, inplace=True)
print(df.to_string())

# 使用 12345 替换 PID 为空数据
df = pd.read_csv('property-data.csv')
df['PID'].fillna(12345, inplace=True)
print(df.to_string())

# 使用 mean() 方法计算列的均值并替换空单元格
df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].mean()
df["ST_NUM"].fillna(x, inplace=True)
print(df.to_string())

# 使用 median() 方法计算列的中位数并替换空单元格
df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].median()
df["ST_NUM"].fillna(x, inplace=True)
print(df.to_string())

# 使用 mode() 方法计算列的众数并替换空单元格
df = pd.read_csv('property-data.csv')
x = df["ST_NUM"].mode()
df["ST_NUM"].fillna(x, inplace=True)
print(df.to_string())

# 第三个日期格式错误
data = {
    "Date": ['2020/12/01', '2020/12/02', '20201226'],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())

# 替换（或者删除）错误年龄的数据
person = {
    "name": ['Google', 'Runoob', 'Taobao'],
    "age": [50, 40, 12345]  # 12345 年龄数据是错误的
}
df = pd.DataFrame(person)
# df.loc[2, 'age'] = 30  # 修改数据
for x in df.index:
    if df.loc[x, "age"] > 120:
        # df.loc[x, "age"] = 120
        df.drop(x, inplace=True)
print(df.to_string())

# 如果对应的数据是重复的，duplicated() 会返回 True，否则返回 False
person = {
    "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
    "age": [50, 40, 40, 23]
}
df = pd.DataFrame(person)
print(df.duplicated())
# 删除重复数据
df.drop_duplicates(inplace=True)
print(df)
