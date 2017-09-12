from mail import Mail
from server import Server

mail = Mail()
mail.printvalue()
mail.sendmessage()
smtp_server, port, from_addr, password, to_address_list = mail.returninfo()
server = Server(smtp_server, port, from_addr, password, to_address_list)
server.login()
server.transmission(mail.returnf())
server.logout()