import config
import weather_ru
import weather_en
import weather_tr
import weather_kg
def getInfo(message):
    try:
        if config.lang == "en":
            config.answer_1 = getCurrent_en(message)
            config.answer_2 = getWeekly_en(message)
        elif config.lang == "ru":
            config.answer_1 = getCurrent_ru(message)
            config.answer_2 = getWeekly_ru(message)
        elif config.lang == "tr":
            config.answer_1 = getCurrent_tr(message)
            config.answer_2 = getWeekly_tr(message)
        else:
            config.answer_1 = getCurrent_kg(message)
            config.answer_2 = getWeekly_kg(message)
    except:
        config.answer_1 = config.vocabulary['en'][4]
        config.answer_2 = config.vocabulary['en'][6]

    return config.answer_1, config.answer_2
#----------------------------------------------------------------------------
def getWeekly_en(message):
    try:
        config.answer = weather_en.get_weekly_info_en()
    except:
        config.answer = config.vocabulary['en'][6]
    return config.answer
def getCurrent_en(message):
    try:
        config.answer = weather_en.weather_info_en(config.old_city)
    except:
        config.answer = config.vocabulary['en'][4]
    return config.answer

#----------------------------------------------------------------------------
def getWeekly_ru(message):
    try:
        config.answer = weather_ru.get_weekly_info_ru()
    except:
        config.answer = config.vocabulary['ru'][6]
    return config.answer
def getCurrent_ru(message):
    try:
        config.answer = weather_ru.weather_info_ru(config.new_city)
    except:
        config.answer = config.vocabulary['ru'][4]
    return config.answer

#----------------------------------------------------------------------------
def getWeekly_tr(message):
    try:
        config.answer = weather_tr.get_weekly_info_tr()
    except:
        config.answer = config.vocabulary['tr'][6]
    return config.answer
def getCurrent_tr(message):
    try:
        config.answer = weather_tr.weather_info_tr(config.old_city)
    except:
        config.answer = config.vocabulary['tr'][4]
    return config.answer

#----------------------------------------------------------------------------
def getWeekly_kg(message):
    try:
        config.answer = weather_kg.get_weekly_info_kg()
    except:
        config.answer = config.vocabulary['kg'][6]

    return config.answer
def getCurrent_kg(message):
    try:
        config.answer = weather_kg.weather_info_kg(config.old_city)
    except:
        config.answer = config.vocabulary['kg'][4]
    return config.answer

