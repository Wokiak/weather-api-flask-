from flask import Flask
import json
import requests

api_key = '6515bb3582e8427298c0c38d2ada0508'
defolt_url = "https://api.openweathermap.org/data/2.5/weather?"


app = Flask(__name__)

temp_city = "Tashkent"
url = defolt_url + "q=" + temp_city + "&units=metric" + "&appid=" + api_key



@app.route("/")
def index():
   # city = request.args.get('city')
   response = requests.get(url)
   if response.status_code == 200:
      data = response.json()   
      main = data['main']
      temperature = main['temp']  
      humidity = main['humidity']  
      pressure = main['pressure']  
      report = data['weather']
      final_data = "Your city is : " + temp_city + "\n" + f"Temperature: {temperature}" + "\n" + f"Humidity: {humidity}" + "\n"  + f"Pressure: {pressure}" + "\n" + f"Weather Report: {report[0]['description']}"   

   return ( "Hello , the temperature of ur city is " + temp_city + final_data)




