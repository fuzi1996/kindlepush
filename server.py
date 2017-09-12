import smtplib
from mail import Mail

class Server():
    def __init__(self,smtp_server,port,from_addr,password,to_address_list):
        self.smtp_server = smtp_server
        self.port = port
        self.from_addr = from_addr
        self.password = password
        self.to_address_list = to_address_list
        self.server = smtplib.SMTP(self.smtp_server, self.port)

    def login(self):
        print("正在建立传输")
        self.server.starttls()
        self.server.set_debuglevel(0)
        print("用户正在登陆")
        self.server.login(self.from_addr, self.password)
        print("用户登陆成功")

    def transmission(self,func):
        self.server.sendmail(self.from_addr, self.to_address_list,func)
        print("传输完成")

    def logout(self):
        print("正在登出服务器")
        self.server.quit()
        print("服务器成功退出")
