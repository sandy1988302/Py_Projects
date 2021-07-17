import os

path = r'D:\Py_Projects\AUTO_CASE\mu1'
'''
for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
'''

for foldName, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if filename != r'a.txt':                             # 筛选出文件名不为a.txt的文件
            if filename.endswith('.txt'):                    # 筛选出后缀为txt的文件
                os.remove(os.path.join(foldName, filename))  # 将文件名与文件所处的目录拼接为完整的文件路径，进行删除
                print("{} 已删除.".format(os.path.join(foldName, filename)))

'''
for foldName, subfolders, filenames in [('foldName1', 'subFolder1', 'a'),
                                        ('foldName1', 'subFolder1', 'b'),
                                        ('foldName3', 'subFolder3', 'c'),
                                        ('foldName4', 'subFolder4', 'd')]:
    for filename in filenames:
        print(foldName)
        print(subfolders)
        print(filenames)
        print(filename)
        print('*' * 12)
        if filename != r'a.txt':
            if filename.endswith('.txt'):
                os.remove(os.path.join(foldName, filename))
                print("{} 已删除.".format(os.path.join(foldName, filename)))
'''