from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

WEATHER_API_ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather'
API_KEY = '0a9d48239b15a060da1987896755ce39'

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Get temperature in Celsius
        }
        response = requests.get(WEATHER_API_ENDPOINT, params=params)
        data = response.json()

        if response.status_code == 200:
            country_name = data['sys']['country']
            temp_celsius = data['main']['temp']
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            coordinate = f"{data['coord']['lon']}, {data['coord']['lat']}"

            weather_data = {
                'country_name': country_name.upper(),
                'temp_celsius': f"{temp_celsius}°C",
                'pressure': f"{pressure} hPa",
                'humidity': f"{humidity}%",
                'coordinate': coordinate
            }
            return render_template('index.html', data=weather_data)
        else:
            return render_template('index.html', error="Failed to retrieve weather data")

    return render_template('index.html', data=None)

@app.route('/logo')
def logo():
    return render_template('logo.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
