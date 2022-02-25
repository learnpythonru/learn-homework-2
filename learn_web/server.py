import json
from pprint import pprint
from textwrap import indent
from flask import Flask
from weather import weather_by_city
app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city("Moscow,Russia")
    if weather:
        with open("test.json", "w") as file:
            print(json.dumps(weather, indent=4),file=file)
        return f"Сейчас {weather['data']['current_condition'][0]['temp_C']}, ощущается как {weather['data']['current_condition'][0]['FeelsLikeC']}"
    else:
        return "Прогноз сейчас недоступен"

if __name__=="__main__":
    app.run(debug=True)
