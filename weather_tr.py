import requests
import json
import datetime
from weather_ru import get_wind
import locale
import config

def weather_info_tr(city_name):
    params = {'APPID': config.API_WEATHER, 'q': city_name, 'units': 'metric', 'lang': 'tr'}
    result = requests.get(config.URL, params=params)
    weather = result.json()
    wind_answer = get_wind(int(weather["wind"]['deg']))
    if weather["main"]['temp'] < 0:
        status = "Hava çok soğuk!🥶"
    elif weather["main"]['temp'] < 15:
        status = "Hava serin 🙄"
    elif weather["main"]['temp'] > 38:
        status = "Hava sıcak☀️"
    else:
        status = "Şimdi hava harika!😙"

    config.lat = weather['coord']['lat']
    config.lon = weather['coord']['lon']
    answer = str(city_name) + " şehrinde:\n\n"
    answer += "Şimdi " + str(weather['weather'][0]["description"]) + "\n\n"
    answer += "Sıcaklık " + str(int(weather["main"]['temp'])) + " °C\n\n"
    answer += "Hissedilen sıcaklık: " + str(int(weather["main"]['feels_like'])) + " °C\n\n"
    answer += "Rüzgar: " + wind_answer + str(round(float(weather['wind']['speed']),1)) + " m/s hızla esiyor \n\n"
    answer += "Basınç " + str(int(weather['main']['pressure'])) + "hPa\n\n"
    answer += "Nem %" + str(int(weather['main']['humidity'])) + "\n\n"
    answer += "Görünürlük: " + str(int(weather['visibility']/1000)) + " km\n\n"
    answer += "Bulutluluk %" + str(int(weather["clouds"]['all'])) + "\n\n" + status+"\n"
    params.clear()
    return answer
def get_weekly_info_tr():
    url2 = config.URL2 % (config.lat, config.lon, config.API_WEATHER2, "tr")
    result1 = requests.get(url2)
    weather1 = json.loads(result1.text)
    locale.setlocale(locale.LC_ALL, "tr")
    now = datetime.datetime.now()
    one_day = datetime.timedelta(1)
    answer = "<b>"+config.vocabulary['tr'][1]+"</b>"+":\n\n"
    for line in weather1["daily"]:
        wind_answer1 = get_wind(int(line['wind_deg']))
        answer += "<b>"+now.strftime("%a") +"</b>"+" - " + "<b>"+now.strftime("%d/%m")+"</b>" + ":\n" + str(int((line['temp']['max']))) + "/" + str(
            int((line['temp']['min']))) + "°C, " + str((line['weather'][0]['description'])) + ", " + str(
            wind_answer1) + str(round(float(line["wind_speed"]),1)) + " m/s\n\n"
        now = now + one_day
    del config.lat
    del config.lon
    return answer

