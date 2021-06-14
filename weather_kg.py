import requests
from googletrans import Translator
import json
import datetime
import locale
import config
from weather_ru import get_wind
def weather_info_kg(city_name):
    params = {'APPID': config.API_WEATHER, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
    result = requests.get(config.URL, params=params)
    weather = result.json()
    wind_answer = get_wind(int(weather["wind"]['deg']))
    kotoruuchu = Translator()
    text1 = str(weather['weather'][0]["description"])
    kotor = kotoruuchu.translate(text1, src='ru', dest='ky')
    if weather["main"]['temp'] < 0:
        status = "Аба суук!🥶"
    elif weather["main"]['temp'] < 15:
        status = "Аба анча суук эмес 🙄"
    elif weather["main"]['temp'] > 38:
        status = "Аба ысык☀️"
    else:
        status = "Азырынча аба-ырайы эң жакшы!😙"

    config.lat = weather['coord']['lat']
    config.lon = weather['coord']['lon']
    answer = str(city_name) + " шаарында: \n\n"
    answer += "Азыркы учурда " + kotor.text +"\n\n"
    answer += "Температура " + str(int(weather["main"]['temp'])) + " °C\n\n"
    answer += "Сезилген температура " + str(int(weather["main"]['feels_like'])) + " °C\n\n"
    answer += "Шамал: " + wind_answer + str(round(float(weather['wind']['speed']),1)) + " м / сек\n\n"
    answer += "Абанын басымы " + str(round(int(weather['main']['pressure'])*0.75,0)) + " мм рт.ст.\n\n"
    answer += "Абанан нымдуулугу " + str(int(weather['main']['humidity'])) + "%" + "\n\n"
    answer += "Көрүнүү абалы " + str(int(weather['visibility']/1000)) + " км\n\n"
    answer += "Булуттуулук " + str(int(weather["clouds"]['all'])) + " %" + "\n\n" + status+"\n"
    params.clear()
    return answer
def get_weekly_info_kg():
    url2 = config.URL2 % (config.lat, config.lon, config.API_WEATHER2, 'ru')
    result1 = requests.get(url2)
    weather1 = json.loads(result1.text)
    locale.setlocale(locale.LC_ALL, "ru")
    now = datetime.datetime.now()
    one_day = datetime.timedelta(1)
    answer = "<b>"+config.vocabulary['kg'][1]+"</b>"+":\n\n"
    for line in weather1["daily"]:
        wind_answer1 = get_wind(int(line['wind_deg']))
        kotoruuchu = Translator()
        text1 = str((line['weather'][0]['description']))
        kotor = kotoruuchu.translate(text1, src='ru', dest='ky')
        answer += "<b>"+now.strftime("%a") +"</b>"+" - " + "<b>"+now.strftime("%d/%m")+"</b>" + ":\n" + str(int((line['temp']['max']))) + "/" + str(
            int((line['temp']['min']))) + "°C, " + kotor.text + ", " + str(
            wind_answer1) + str(round(float(line["wind_speed"]),1)) + " м/с\n\n"
        now = now + one_day
    del config.lat
    del config.lon
    return answer
