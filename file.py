import os
import os.path
import time
import sys
# 这个文件实现文件打开，判断文件大小功能

class Fileor():
    def __init__(self,path):
        self.path = path

    def file_walk(self):
        size = 0
        for dirn,r2,fname in os.walk(self.path):
            for i in fname:
                size += os.path.getsize(dirn +"//"+ i)
            return dirn,fname,size

    def otfile(self):
        #返回值依次为书名，格式，文件完整路径
        st = []
        mt = []
        completepath = []
        path,filelist,file_size_sum = Fileor.file_walk(self)
        if file_size_sum >= 25000000:
            print("所选择文件总大小不得大于25M\n")
            print("请关闭该窗口，减少文件数量，以满足要求")
            time.sleep(5)
            sys.exit()
        else:
            for i in range(len(filelist)):
                strr = filelist[i]
                completepath.append(path+"\\"+ strr)
                st.append(strr.split(".")[0])
                mt.append(strr.split(".")[1])
            return st,mt,completepath





































































