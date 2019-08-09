import requests
import json

##	LEER IP DEL SERVIDOR
f=open("ip_config.txt", "r")
ip = str(f.read())
f.close()
url = ip + '/rest/login'

parametros = {'USUARIO':'pdestrad@gmail.com', 'CONTRASENA': 'homoplato1'}
r = requests.post(url, data=json.dumps(parametros))
respuesta = json.dumps(r.json())
print(respuesta)