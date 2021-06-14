import requests
import json
import datetime
import locale
import config
def weather_info_ru(city_name):
    params = {'APPID': config.API_WEATHER, 'q': city_name, 'units': 'metric', 'lang': "ru"}
    result = requests.get(config.URL, params=params)
    weather = result.json()
    wind_answer = get_wind(int(weather["wind"]['deg']))
    if weather["main"]['temp'] < 0:
        status = "Сейчас холодно!🥶"
    elif weather["main"]['temp'] < 10:
        status = "Терпимо!😬"
    elif weather["main"]['temp'] < 15:
        status = "Прохладно!🙄"
    elif weather["main"]['temp'] > 30:
        status = "Сейчас жарко!☀️"
    else:
        status = "Сейчас отличная температура! 😙"
    config.lat = weather['coord']['lat']
    config.lon = weather['coord']['lon']
    answer = "В городе " + str(city_name) + ":\n\n"
    answer += "Сейчас " + str(weather['weather'][0]["description"]) + "\n\n"
    answer += "Температура " + str(int(weather["main"]['temp'])) + " °C\n\n"
    answer += "Чувствуется как " + str(int(weather["main"]['feels_like'])) + " °C\n\n"
    answer += "Ветер: " + wind_answer + str(float(weather['wind']['speed'])) + " м/сек\n\n"
    answer += "Давление " + str(round(int(weather['main']['pressure'])*0.75,0)) + " мм рт.ст.\n\n"
    answer += "Влажность " + str(int(weather['main']['humidity'])) + "%" + "\n\n"
    answer += "Видимость " + str(int(weather['visibility']/1000)) + " км\n\n"
    answer += "Облачность " + str(int(weather["clouds"]['all'])) + " %" + "\n\n" + status +"\n"
    return answer

def get_weekly_info_ru():
    url2 = config.URL2 % (config.lat, config.lon, config.API_WEATHER2, 'ru')
    result1 = requests.get(url2)
    weather1 = json.loads(result1.text)
    locale.setlocale(locale.LC_ALL, "ru")
    now = datetime.datetime.now()
    one_day = datetime.timedelta(1)
    answer = "<b>"+config.vocabulary['ru'][1]+"</b>"+":\n\n"
    for line in weather1["daily"]:
        wind_answer1 = get_wind(int(line['wind_deg']))
        answer += "<b>"+now.strftime("%a") +"</b>"+" - " + "<b>"+now.strftime("%d/%m")+"</b>" + ":\n" + str(int((line['temp']['max']))) + "/" + str(
            int((line['temp']['min']))) + "°C, "+str((line['weather'][0]['description']))+", "+str(
            wind_answer1)+str(round(float(line["wind_speed"]),1))+" м/с\n\n"
        now = now + one_day
    del config.lat
    del config.lon
    return answer

def get_wind(wind):
    if 23 <= wind < 68:
        wind_answer = " ↙️ "
    elif 68 <= wind < 112:
        wind_answer = " ⬅️ "
    elif 112 <= wind < 157:
        wind_answer = " ↖️ "
    elif 157 <= wind < 202:
        wind_answer = " ⬆️ "
    elif 202 <= wind < 247:
        wind_answer = " ↗️ "
    elif 247 <= wind < 292:
        wind_answer = " ➡️ "
    elif 292 <= wind < 337:
        wind_answer = " ↘️ "
    else:
        wind_answer = " ⬇️ "
    return wind_answer