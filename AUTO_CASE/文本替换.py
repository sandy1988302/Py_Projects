def file_replace(filename, repword, newword):
    f_read = open(filename)
    content = []
    count = 0
    for each_line in f_read:
        if repword in each_line:
            count = count + each_line.count(repword)
            each_line = each_line.replace(repword, newword)
        content.append(each_line)

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' %
                   (filename, count, repword, repword, newword))
    if decide in ['YES', 'Yes', 'yes']:
        f_write = open(filename, 'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()


file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)
