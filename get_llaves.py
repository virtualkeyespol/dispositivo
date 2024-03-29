import requests
import json
import os
import time

import led as LED

##	LEER IP DEL SERVIDOR
files_path = os.getcwd() + '/files'
f=open(files_path + "/ip_config.txt", "r")
ip = str(f.read())
f.close()
url = ip + '/rest/llave/read_llaves_dispositivo'

while True:
	try:
		##	LEER NUMERO DE SERIE DEL DISPOSITIVO
		f=open("files/numero_serie.txt", "r")
		NUMERO_SERIE = str(f.read())
		f.close()

		## REALIZAR REQUEST
		parametros = {"NUMERO_SERIE" : NUMERO_SERIE}
		r = requests.get(url, params=parametros)

		if r.status_code == 200:
			## VERIFICANDO RESPUESTA DEL SERVIDOR
			respuesta = json.loads(r.text)
			if respuesta["STATUS"] == "OK":
				##	GUARDANDO LLAVES
				llaves = {}
				f=open("files/llaves.txt", "w+")
				respuesta = json.loads(r.text)
				print(respuesta)
				for llave in respuesta["RESPUESTA"]:
					llaves[llave["codigo"]] =  {
						"fecha_expiracion" : llave["fecha_expiracion"],
						"fecha_inicio" : llave["fecha_inicio"]
					}
				
				f.write(json.dumps(llaves))
				f.close()

				## MOSTRAR ESTADO ACTUALIZADO
				LED.actualizado()
			else:
				print("ERROR")
		else:
			## MANEJO DE ERROR DE REQUEST
			print("ERROR DE REQUEST")

	except Exception as e:
		## MANEJO DE ERROR EN LECTURA DE NUMERO DE SERIE
		print("ERROR EN LECTURA DE NUMERO DE SERIE " + str(e))

	time.sleep(5)
	