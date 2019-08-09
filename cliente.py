import requests
import json

##	LEER NUMERO DE SERIE DEL DISPOSITIVO
f=open("ip_config.txt", "r")
ip = str(f.read())
f.close()

print(ip)

parametros = {'USUARIO':'pdestrad@gmail.com', 'CONTRASENA': 'homoplato1'}
url = ip + '/rest/login'
r = requests.post(url, data=json.dumps(parametros))
respuesta = json.dumps(r.json())
print(respuesta)