"""
Este Archivo llamado api.py fue el utilizado para hacer las pruebas unitarias,
Utilisamos este para poder tener una utilizacion mas facil de las variables a usar.
"""

"""
:pyown libreria: Libreria utilizada para el uso de las Api
"""
import pyowm

"""
:var own: Aqui se esa guardando la api 'ce688b67bbf90c2a0236d4eb23d8c7bd',
que despues sera utilizada
"""
owm = pyowm.OWM('ce688b67bbf90c2a0236d4eb23d8c7bd')

"""
:var observation: Es la utilizada para buscar la cuidad o el pais.
"""
observation = owm.weather_at_place('argentina')
w = observation.get_weather()

estatus=w.get_status()
time=w.get_sunset_time('iso')
viento=(w.get_wind()['speed'])
tempe=w.get_temperature('celsius')['temp']
tempe1=w.get_temperature('celsius')['temp_max']
tempe2=w.get_temperature('celsius')['temp_min']
l = observation.get_location()
lugar = l.get_country()
hume=w.get_humidity()

"""
print("Lugar ",lugar)
print("Estatus ",estatus)
print("Viento ",viento)     #Viento
print("Humedad ",hume)
print("Temp normal ",tempe)        #Temp Normal
print("Temp Max ",tempe1)       #Temp Max
print("Temp Min ",tempe2)       #Temp Min
"""