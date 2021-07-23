import datetime

import requests

s_city = "Tula"
city_id = 480562
APPID = "5295fc96cbb9ed91b0e83b0ee42d0507"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'appid': APPID})
data = res.json()
item_list = {'coord': 'Координаты', 'weather': 'Погода', 'main': 'Главное', 'wind': 'Ветер', 'clouds': 'Облака',
             'sys': 'Системные'}
item_trans = {'base': 'База', 'visibility': 'Видимость', 'timezone': 'Временная зона', 'id': 'ИД', 'name': 'Город'}
items = []

for item in data:
    if item in item_list:
        print('----------------\n' + item_list[item], '\n')
        for item2 in data[item]:
            if type(item2) == dict:
                for item3 in item2:
                    print(item3, item2[item3])
            else:
                if 'sun' in item2:
                    data[item][item2] = str(datetime.datetime.fromtimestamp(data[item][item2]))
                print(item2, data[item][item2])
        print()
    elif item in item_trans:

        print(item_trans[item], data[item])
    else:

        print(item, data[item])

