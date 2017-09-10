from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib
from file import Fileor

def input_template(s):
    return input("请输入" + s)

def print_tempalte(s1,s2):
    return print("您输入的" + s1 + "是" + s2)

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(((Header(name,'utf-8').encode()),addr))


class Mail():
    def __init__(self):
        self.from_addr = input_template("发送方邮箱账号:")
        self.password = input_template("发送方密码:")
        yes_or_no = True
        self.to_address_list = []
        while yes_or_no:
            to_addr = input_template("接收方邮箱账号:")
            self.to_address_list.append(to_addr)
            yes_or_no = input("是否继续输入(y/n):")
            if yes_or_no == ("y"or"yes"):
                pass
            else:
                yes_or_no = False
        self.smtp_server = input_template("邮件服务器地址:")
        self.port = input_template("邮箱SMTP端口(ssl):")
        self.bookpath = input_template("存储书籍目录:")

    def printvalue(self):
        print_tempalte("发送方邮箱账号",self.from_addr)
        print_tempalte("发送方密码",self.password)
        print_tempalte("接收方邮箱账号",str(self.to_address_list).strip("[]"))
        print_tempalte("邮件服务器地址",self.smtp_server)
        print_tempalte("邮箱SMTP端口(ssl)",self.port)
        print_tempalte("存储书籍目录", self.bookpath)

    def sendmessage(self):
        msg = MIMEMultipart()
        msg['Subject'] = Header('convert', 'utf-8').encode()
        fileobj = Fileor(self.bookpath)
        booknamelist, suffixnamelist, completepathlist = fileobj.otfile()
        for bookname, suffixname, completepath in zip(booknamelist, suffixnamelist, completepathlist):
            with open(completepath, 'rb') as f:
                # 设置附件的MIME和文件名:
                mime = MIMEBase(suffixname,"octet-stream")
                # 加上必要的头信息:
                mime.add_header('Content-Disposition', 'attachment', filename= bookname + "." + suffixname)
                # 把附件的内容读进来
                mime.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(mime)
                # 添加到MIMEMultipart:
                msg.attach(mime)
        return msg

    def loginout(self):
        print("正在登陆")
        server = smtplib.SMTP(self.smtp_server,self.port)
        print("服务器登陆成功")
        print("正在建立传输")
        server.starttls()
        server.set_debuglevel(1)
        print("用户正在登陆")
        server.login(self.from_addr,self.password)
        print("用户登陆成功")
        server.sendmail(self.from_addr,self.to_address_list,Mail.sendmessage(self).as_string())
        print("传输完成")
        print("正在登出服务器")
        server.quit()
        print("服务器成功退出")

if __name__ == "__main__":
    mail = Mail()
    mail.loginout()



