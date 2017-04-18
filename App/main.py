from flask import Flask
from flask import render_template
from flask import request
import pyowm

owm=pyowm.OWM('ce688b67bbf90c2a0236d4eb23d8c7bd')

App=Flask(__name__)

@App.route('/')
def index():
    return render_template('index.html')

@App.route('/temperatura',methods=['POST'])
def temperatura():
    clima=request.form['ciudad']
    observation = owm.weather_at_place(clima)
    tomorrow = pyowm.timeutils.tomorrow()
    w = observation.get_weather()
    wind=w.get_wind()['speed']
    humi=w.get_humidity()
    estatus = w.get_status()
    print(estatus)
    l = observation.get_location()
    lugar = l.get_country()
    tem1 = w.get_temperature('celsius')['temp_max']
    tem2 = w.get_temperature('celsius')['temp_min']
    tem3 = w.get_temperature('celsius')['temp']

    return render_template('temperatura.html',wi=wind, hu=humi,nom=clima,
                           tomo=tomorrow,temp1=tem1,temp2=tem2,temp3=tem3,
                           esta=estatus,lugarr=lugar)
if __name__=="__main__":
    App.run()