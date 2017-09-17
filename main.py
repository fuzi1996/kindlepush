from mail import Mail
from server import Server
from infocon import InforInput,JsonLoad
import os.path
import sys


class Main(object):
    def __init__(self):
        if os.path.exists("config.json"):
            print("已检测到存储的密码")
            self.from_addr = JsonLoad()["from_addr"]
            self.password = JsonLoad()["password"]
            self.to_address_list = JsonLoad()["to_address_list"]
            self.port = JsonLoad()["port"]
            self.smtp_server = JsonLoad()["smtp_server"]
            self.bookpath = input("请输入存储书籍目录(是目录不是文件):")
        else:
            inforinput = InforInput()
            inforinput.JsonStorage()
            self.bookpath = input("请输入存储书籍目录(是目录不是文件):")
        self.mail = Mail(self.from_addr,self.password,self.to_address_list,self.port,self.smtp_server,self.bookpath)
        self.mail.printvalue()

    def transfile(self):
        yesorno = input("如果无误，请输入y,如果错误请删除文件config.json,再重新运行此程序\n")
        if yesorno == ("y" or "yes"):
            self.mail.sendmessage()
            self.server = Server(self.smtp_server, self.port, self.from_addr, self.password, self.to_address_list)
            self.server.login()
            self.server.transmission(self.mail.returnf())
        else:
            sys.exit()

yon = "y"
while yon == ("y" or "yes"):
    main = Main()
    main.transfile()
    yon = input("是否继续(y/n)？")
    if yon == "n":
        main.server.logout()




