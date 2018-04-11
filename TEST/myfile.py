# coding=utf-8
import os
def integrate(filedir):
    filenames = os.listdir(filedir)
    f = open('result.txt', 'w')
    for filename in filenames:
        filepath = filedir + '/' + filename
        for line in open(filepath):
            str = line[0:]
            str.strip()
            str.format
            # print(str)
            f.writelines(str)
    f.close()
    return 'result.txt'
# 对齐格式
def form(filename):

    f = open('mod_result.txt', 'w')
    for line in open(filename):
        tmp = line.split("\t")
        print(tmp)
        temp = tmp[2].split(" ")
        print(tmp[1], str(temp[0]).replace("-", ""), str(temp[1]).replace(":", ""))
        f.writelines(tmp[1]+","+str(temp[0]).replace("-", "")+","+str(temp[1]).replace(":", ""))
    f.close()
if __name__ == '__main__':
    filedir = 'G:/huawei/data'
    form(integrate(filedir))
