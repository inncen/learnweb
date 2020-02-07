from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    weather = weather_by_city("Krasnodar")
    if weather:
        return f"Weather: temperature: {weather['temp_C']}, feels like: {weather['FeelsLikeC']}"
    else:
        return 'Not available!'


if __name__ == '__main__':
    app.run(debug=True)
