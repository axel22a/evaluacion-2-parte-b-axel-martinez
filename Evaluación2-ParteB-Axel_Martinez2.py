import urllib.parse 
import requests

los_40_principales = "https://www.mapquestapi.com/directions/v2/route?"
papas = "Yamera"
tomate = "Niamey"
lechuga = "j1Q671neUmn3JxOoWhufqQ3OJf3OJa9l"

while True:
    papas = input("Ciudad de Origen: ")
    if papas == "Salir" or papas == "s":
        break

    tomates = input("Ciudad de Destino: ")
    if tomates == "Salir" or tomates == "s":
        break

    url = los_40_principales + urllib.parse.urlencode({"key" :lechuga, "from" :papas, "to" :tomates})

    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_status = json_data ["info"] ["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = llamado de la ruta exitosa.\n")
        print("=============================================")
        print("direcciones de " + (papas) + " a " + (tomates))
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