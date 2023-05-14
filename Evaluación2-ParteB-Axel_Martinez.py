import urllib.parse 
import requests

api_principal = "https://www.mapquestapi.com/directions/v2/route?"
origen = "Yamera"
destino = "Niamey"
llave = "j1Q671neUmn3JxOoWhufqQ3OJf3OJa9l"

while True:
    origen = input("Ciudad de Origen: ")
    if origen == "Salir" or origen == "s":
        break

    destino = input("Ciudad de Destino: ")
    if destino == "Salir" or destino == "s":
        break

    url = api_principal + urllib.parse.urlencode({"key" :llave, "from" :origen, "to" :destino})

    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_status = json_data ["info"] ["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = llamado de la ruta exitosa.\n")
        print("=============================================")
        print("direcciones de " + (origen) + " a " + (destino))
        print("duracion del viaje:   " + (json_data["route"]["formattedTime"]))
        print("kilometros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        for cada in json_data["route"]["legs"][0]["maneuvers"]:
            print((cada["narrative"]) + " (" + str("{:.2f}".format((cada["distance"])*1.61) + " km)"))
            print("=============================================\n")
        
    elif json_status == 402:
         print("**********************************************")
         print("codigo de estado: " + str(json_status) + "; una o ambas localizaciones ingresadas son invalidas.")
         print("**********************************************\n")
    elif json_status == 611:
         print("**********************************************")
         print("codigo de estado: " + str(json_status) + "; falta una o ambas localizaciones.")
         print("**********************************************\n")
    else:
         print("************************************************************************")
         print("para codigo de estado: " + str(json_status) + "; referirse a:")
         print("https://developer.mapquest.com/documentation/directions-api/status-codes")
         print("************************************************************************\n")