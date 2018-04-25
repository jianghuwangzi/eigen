#!/usr/bin/python
# -*- coding: UTF-8 -*-
def getfilelines(filename, eol='\n', buffsize=4096):
    """计算给定文件有多少行"""
    with open(filename, 'rb') as handle:
        linenum = 0
        buffer = handle.read(buffsize)
        while buffer:
            linenum += buffer.count(eol)
            buffer = handle.read(buffsize)
        return linenum+1#返回总行数，如果是7的话， 实际是0-6
if __name__ == "__main__":
    import linecache
    import random
    need_line=1000#要取的总行数
    f='big_data.txt'# file name
    # dict1={}
    # dict1=dict1.fromkeys(range(need_line), [])  # 建立空字典
    list1=[[] for i in xrange(need_line)]# 建立need_line个空list
    # print list1
    # print getfilelines('big_data_test')
    totle=getfilelines(f)
    for line_hash in range(1,totle+1):
        # print line_hash
        mod_hash = line_hash % need_line
        # print mod_hash,
        # print type(mod_hash)
        # print line_hash,
        # print type(line_hash)
        list1[mod_hash].append(line_hash)
        # print list1
    # print list1
    list2=[]#存储要提取的行号
    for line in range(need_line):
        # print line
        # k = random.randint(1,len(list1[line]))
        # print k
        # print list1[line][k-1]
        list2.append(list1[line][random.randint(1,len(list1[line]))-1])
        # print list1[line[k]]
        # list2.append(random(list1[line]))
    # print list2
    # list2.sort()#可以进行升序排序输出
    for need in list2:
        line = linecache.getline(f, need)
        print line,