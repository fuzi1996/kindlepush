import json


def input_template(s):
    return input("请输入" + s)

def print_tempalte(s1, s2):
    return print("您输入的" + s1 + "是" + s2)

def JsonLoad():
    with open("config.json","rb") as f:
        d = json.load(f)
    return d

class InforInput(object):
    def __init__(self):
        self.from_addr = input_template("发送方邮箱账号:")
        self.password = input_template("发送方密码:")
        yes_or_no = True
        self.to_address_list = []
        while yes_or_no:
            to_addr = input_template("接收方邮箱账号:")
            self.to_address_list.append(to_addr)
            yes_or_no = input("是否继续输入(y/n):")
            if yes_or_no == ("y" or "yes"):
                pass
            else:
                yes_or_no = False
        self.smtp_server = input_template("邮件服务器地址:")
        self.port = input_template("邮箱SMTP端口(ssl):")


    def JsonStorage(self):
        d = {
            "from_addr" : self.from_addr,
            "password" : self.password,
            "to_address_list" : self.to_address_list,
            "smtp_server" : self.smtp_server,
            "port" : self.port,
        }
        with open("config.json","w") as f:
            json.dump(d, f)
            f.close()
    def inforreturn(self):
        return self.from_addr,self.password,self.to_address_list,self.to_address_list,self.smtp_server,self.port




if __name__ == "__main__":
    inforinput = InforInput()
    inforinput.JsonStorage()











