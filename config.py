TOKEN = '1703387044:AAFhHr0fwKg4cmN3Oy9peGbFxcWsrsmAH_U'
URL = 'http://api.openweathermap.org/data/2.5/weather'
API_WEATHER ='5b67cb156ecfee9cdeafdabe9db6975f'
API_WEATHER2 = '1ef59eb8413621790ab7ecc600010dcd'
URL2 = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric&lang=%s"
lang = 'en'
old_city = ''
new_city = ''
lat = ''
lon = ''
answer_1 = ''
answer_2 = ''
answer = ''
vocabulary = {'en': ["Current", "Weekly", "New city", "Change language","City not found",
                     "Write the city", "Please try again", "Selected language: English\n"],
              "ru": ['Текущая', "Недельная", "Новый город","Поменять язык", "Город  не найден",
                     "Введите город","Попробуйте ещё раз", "Выбран язык: Русский\n"],
              "kg": ["Азыркы", "Бир жумалык","Жаңы шаар","Тилди алмаштыруу", "Шаар табылган жок",
                     "Шаарды киргизиңиз","Кайра териңиз","Тандалган тил: Кыргыз тили\n"],
              "tr": ["Şu anki", "Haftalık", "Yeni şehir", "Dili değiştir","Şehir bulunamadı",
                     "Şehiri yazınız","Lütfen tekrar deneyin", "Seçilen dil: Türk dili\n"]
              }
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяçğıöşüqwertyuiopasdfghjklzxcvbnm- '

menu = "/start - To start the bot\n\n/help - To get instruction\n\n/lang - To change languages\n"

text_tr = 'Ben hava durumunu gösteren basit bir botum. İhtiyacınız olan dili seçin ve şehrin adını yazın.'\
            'Hem güncel hem de haftalık hava durumunu gösterebilirim. \n Şehir adını seçilen dilde doğru ' \
            'yazdığınızdan emin olun, aksi takdirde şehri bulamıyorum ☹️.\nBazı şehirler benim veritabanında olamayacağını anlamalıdır. \n' \
            'Kullanımınızın tadını çıkarın 😇 \n '

text_en = 'I am a simple bot to show the weather. Choose the language you need and write the name of the city. '\
            'I can show both current and weekly weather. \n Make sure you spell the city name correctly ' \
            'in the selected language, otherwise I cannot find the city ☹️.\nYou should understand that some cities cannot be in my database. \n' \
            'Enjoy your use 😇 \n '

text_ru = 'Я простой бот показывающий погоду. Выбери нужный тебе язык и напиши название города. ' \
           'Могу показать как текущую так и недельную погоду.\nУбедись в том, что правильно написал название города ' \
           'в выбронном языке, в противном случае я не смогу найти город ☹️. \nВы должны понять, что некоторые города не могут быть в моём базе данных.\n' \
           'Приятного использования 😇\n'

