import requests
#import settings
from flask import current_app


def wether_by_city(city_name):
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    #url = "http://api.worldweatheronline.com/premium/v1/weather.a"
    param = {
        "key": current_app.config['WEATHER_API_KEY'],
        "q" : city_name,
        "format" : "json",
        "num_of_days" : 1,
        "lang" : "ru"
    }
    try:
        result = requests.get(url,params=param)
        result.raise_for_status()
        wether = result.json()
        if 'data' in wether:
            if 'current_condition' in wether['data']:
                try:
                    return(wether['data']['current_condition'][0])
                except(IndexError,TypeError):
                    return False
    except(requests.RequestException,ValueError):
    #except(requests.RequestException):
        print('Network Error')
        return False
    return False

if __name__ == '__main__':
    w = wether_by_city(current_app.config['WEATHER_CITY'])
    print(w)