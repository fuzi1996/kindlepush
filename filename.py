from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib
import os
import os.path
import time
import sys

to_address_list = []

def input_template(s):
    return input("请输入" + s)

def print_tempalte(s1,s2):
    return print("您输入的" + s1 + "是" + s2)

from_addr = input_template("发送方邮箱账号:")


password = input_template("发送方密码:")


yes_or_no = True
while yes_or_no:
    to_addr = input_template("接收方邮箱账号:")
    to_address_list.append(to_addr)
    yes_or_no = input("是否继续输入(y/n):")
    if yes_or_no == ("y"or"yes"):
        pass
    else:
        yes_or_no = False
smtp_server = input_template("请输入邮件服务器地址")
print_tempalte("发送方邮箱账号",from_addr)
print_tempalte("发送方密码",password)
print_tempalte("接收方邮箱账号",str(to_address_list).strip("[]"))
print_tempalte("邮件服务器地址",smtp_server)



def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(((Header(name,'utf-8').encode()),addr))

msg = MIMEMultipart()
msg['From'] = _format_addr('<%s>'% from_addr)
msg['Subject'] = Header('convert','utf-8').encode()

def file_name(file_dir):
    size = 0
    for dirn,r2,fname in os.walk(file_dir):
        for i in fname:
            size += os.path.getsize(dirn +"//"+ i)
        return dirn,fname,size

def otfile(filepath):
    path,filelist,file_size_sum = file_name(filepath)
    print("所选择文件为:" + filepath)
    print("文件数目为:" + str(len(filelist)))
    print("所选择文件大小为"+str(file_size_sum))
    if file_size_sum >= 25000000:
        print("所选择文件总大小不得大于25M\n")
        print("请关闭该窗口，减少文件数量，以满足要求")
        time.sleep(5)
        sys.exit()
    else:
        for i in range(len(filelist)):
            strr = filelist[i]
            completepath = path+"\\"+ strr
            st = strr.split(".")[0]
            mt = strr.split(".")[1]
            with open(completepath,'rb') as f:
                # 设置附件的MIME和文件名:
                mime = MIMEBase("mobi","txt")
                # 加上必要的头信息:
                mime.add_header('Content-Disposition', 'attachment', filename=st +"."+ mt)
                # 把附件的内容读进来
                mime.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart:
                msg.attach(mime)

file_path = input("请输入存放kindle书籍的文件夹路径:")
otfile(file_path)
print("正在登陆")
server = smtplib.SMTP(smtp_server,587)
print("服务器登陆成功")
print("正在建立传输")
server.starttls()
server.set_debuglevel(1)
print("用户正在登陆")
server.login(from_addr,password)
print("用户登陆成功")
server.sendmail(from_addr,to_address_list,msg.as_string())
print("传输完成")
print("正在登出服务器")
server.quit()
print("服务器成功退出")



