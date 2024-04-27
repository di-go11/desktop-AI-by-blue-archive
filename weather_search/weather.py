import requests

class weather():
  
  #apiのカギのインスタンスを生成
  def __init__(self,api_key):
    self.api_key = api_key
  
  #以下のアドレスに投げて返答を返す、モジュール
  def get_weather(self, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data
  
  def print_weather(self, city):
    weather_data = self.get_weather(city)

    if weather_data["cod"] == 200:
        weather_description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        print(f"The weather in {city} is {weather_description}. Temperature: {temperature}°C")
    else:
        print("Failed to retrieve weather data.")
        
# クラスのインスタンスを作成
#weather_getter = weather("8754bbfd042a3807dd3abe54dcc99c87")

# 天気情報を取得して表示
#weather_getter.print_weather("Nagano")