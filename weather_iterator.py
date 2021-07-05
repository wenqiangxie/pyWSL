import json
import urllib.request


class WeatherIterator:
    def __init__(self, city_id="101010100"):
        self.base_url = "http://www.weather.com.cn/data/cityinfo/"
        self.city_id = city_id
        self.url = f"{self.base_url}/{self.city_id}.html"

    def __next__(self):
        try:
            with urllib.request.urlopen(self.url) as f:
                return json.loads(f.read().decode('utf-8'))["weatherinfo"]
        except Exception as exc:
            raise exc


def print_weather(weather: dict):
    print(f"{weather['city']}({weather['cityid']})\t\t{weather['ptime']}")
    print("--------------------------")
    print(f"{weather['weather']}\t\t\t{weather['temp1']}-{weather['temp2']}")
    print("\n\n\n")


if __name__ == '__main__':
    wx = WeatherIterator()

    wx_info = next(wx)
    print_weather(wx_info)
