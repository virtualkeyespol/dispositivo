import bluetooth
import json

url = ip + '/rest/llave/verificar_llave'

def verificar_llave(codigo):
    ## REALIZAR REQUEST
    parametros = {"CODIGO" : codigo}
    r = requests.get(url, params=parametros)
    if r.status_code == 200:
        ## VERIFICANDO RESPUESTA DEL SERVIDOR
        respuesta = json.loads(r.text)
        if respuesta["STATUS"] == "OK":
            LED.abierto()
        else:
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



