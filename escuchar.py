import bluetooth
import json
import requests
import json
import os

import led as LED

##  LEER IP DEL SERVIDOR
files_path = os.getcwd() + '/files'
f=open(files_path + "/ip_config.txt", "r")
ip = str(f.read())
f.close()
url = ip + '/rest/llave/verificar_llave'

def verificar_llave(codigo):
    ## REALIZAR REQUEST
    parametros = {"CODIGO" : codigo}
    r = requests.get(url, params=parametros)
    if r.status_code == 200:
        ## VERIFICANDO RESPUESTA DEL SERVIDOR
        respuesta = json.loads(r.text)
        if respuesta["STATUS"] == "OK":
            print("EXITO")
            LED.abierto()
        else:
            print("FALLO")
            LED.status()
    else:
        ## MANEJO DE ERROR DE REQUEST
        print("ERROR DE REQUEST")


server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()

while 1:
    data = client_socket.recv(1024)
    codigo = str(data)
    print("CODIGO: " + codigo, verificar_llave(codigo))

    if (data == "q"):
        print("Quit")
        break

client_socket.close()
server_socket.close()



