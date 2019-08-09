import requests
import json

##	LEER NUMERO DE SERIE DEL DISPOSITIVO
f=open("ip_config.txt", "r")
ip = str(f.read())
f.close()

print(ip)

parametros = {'USUARIO':'pdestrad@gmail.com', 'CONTRASENA': 'homoplato1'}

r = requests.post('http://127.0.0.1:8000/rest/login', data=json.dumps(parametros))
respuesta = json.dumps(r.json())
print(respuesta)