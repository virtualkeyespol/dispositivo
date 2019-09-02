import bluetooth
import json

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


def verificar_llave(codigo):
    f=open("files/numero_serie.txt", "r")
    string = str(f.read())
    f.close()
    llaves = json.loads(string)
    respuesta = llaves.get(codigo, None)

    print("RESPUESTA ", respuesta)
    
    if respuesta == None:
        return False
    else:
        return True
