from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from file import Fileor

def print_tempalte(s1,s2):
    return print("您输入的" + s1 + "是" + s2)

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(((Header(name,'utf-8').encode()),addr))


class Mail():
    def __init__(self,from_addr,password,to_address_list,smtp_server,port,bookpath):
        self.from_addr = from_addr
        self.password = password
        self.to_address_list = to_address_list
        self.smtp_server = smtp_server
        self.port = port
        self.bookpath = bookpath


    def printvalue(self):
        print("请确认:")
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
    def returnf(self):
        return self.sendmessage().as_string()




# if __name__ == "__main__":
#     mail = Mail()
#     smtp_server, port, from_addr, password, to_address_list = mail.returninfo()
#     server = Server(smtp_server, port, from_addr, password, to_address_list)
#     server.login()
#     server.logout()



