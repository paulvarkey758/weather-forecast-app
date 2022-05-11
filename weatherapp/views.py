from django.shortcuts import render
import requests

# Create your views here.
def mainfun(request):
    return render(request,"index.html")
def showweather(request):
    city=request.GET['cityname']
    try:
        url=f"http://api.weatherapi.com/v1/forecast.json?key=69528a98f894438b88981548221503 &q={city}&days=1&aqi=no&alerts=no"
        data= requests.get(url).json()
        OverallWeather={'location':data['location'],
                        'current':data['current'],
                        'forecast_day':data['forecast']['forecastday'][0]['day'],
                        'forecast_astro':data['forecast']['forecastday'][0]['astro'],
                        'forecast_hour':data['forecast']['forecastday'][0]['hour']
                        
        }

        return render(request,"weather.html",{'weather':OverallWeather})
    except:
        return render(request,"error.html")    
