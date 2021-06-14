import requests
import json
import datetime
import locale
import config
from weather_ru import get_wind


def weather_info_en(city_name):
    params = {'APPID': config.API_WEATHER, 'q': city_name, 'units': 'metric', 'lang': 'en'}
    result = requests.get(config.URL, params=params)
    weather = result.json()
    wind_answer = get_wind(int(weather["wind"]['deg']))
    if weather["main"]['temp'] < 0:
        status = "It's too cold!🥶"
    elif weather["main"]['temp'] < 15:
        status = "It's cool now!🙄"
    elif weather["main"]['temp'] > 38:
        status = "It's hot now!☀️"
    else:
        status = "Now the temperature is great! 😙"
    config.lat = weather['coord']['lat']
    config.lon = weather['coord']['lon']
    answer = "In the city " + str(city_name) + ":\n\n"
    answer += "Temperature is " + str(int(weather["main"]['temp'])) + " °C\n\n"
    answer += "Feels like " + str(int(weather["main"]['feels_like'])) + " °C\n\n"
    answer += "Description: " + str(weather['weather'][0]["description"]) + "\n\n"
    answer += "The wind: " + wind_answer +str(round(float(weather['wind']['speed']),1)) + " m/s\n\n"
    answer += "Pressure " + str(int(weather['main']['pressure'])) + "hPa\n\n"
    answer += "Humidity " + str(int(weather['main']['humidity'])) + "%" + "\n\n"
    answer += "Visibility " + str(int(weather['visibility']/1000)) + " km\n\n"
    answer += "Cloudiness " + str(int(weather["clouds"]['all'])) + " %" + "\n\n" + status +"\n"
    return answer
def get_weekly_info_en():
    url2 = config.URL2 % (config.lat, config.lon, config.API_WEATHER2, 'en')
    result1 = requests.get(url2)
    weather1 = json.loads(result1.text)
    locale.setlocale(locale.LC_ALL, "en")
    now = datetime.datetime.now()
    one_day = datetime.timedelta(1)
    answer = "<b>"+config.vocabulary['en'][1]+"</b>"+":\n\n"
    for line in weather1["daily"]:
        wind_answer1 = get_wind(int(line['wind_deg']))
        answer += "<b>"+now.strftime("%a") +"</b>"+" - " + "<b>"+now.strftime("%d/%m")+"</b>" + ":\n" + str(int((line['temp']['max']))) + "/" + str(
            int((line['temp']['min']))) + "°C, " + str((line['weather'][0]['description'])) + ", " + str(
            wind_answer1) + str(round(float(line["wind_speed"]),1)) + " m/s\n\n"
        now = now + one_day
    del config.lat
    del config.lon
    return answer

def clear_phrase(phrase):
    phrase = phrase.strip()
    phrase = phrase.lower()
    phrase = phrase.replace('ү', 'у')
    phrase = phrase.replace('ө', 'о')
    phrase = phrase.replace('ң', 'н')
    result = ''.join(symbol for symbol in phrase if symbol in config.alphabet)
    result = result.title()
    return result

