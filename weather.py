from flask import Flask, render_template, request
import urllib.request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=0a9d48239b15a060da1987896755ce39'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        country_name = data['sys']['country']
        temp_kelvin = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        coordinate = f'{data["coord"]["lon"]}, {data["coord"]["lat"]}'

        temp_celsius = round(temp_kelvin - 273.15, 1)

        return render_template('index.html',
                               data={'country_name': country_name.upper(),
                                     'temp_celsius': temp_celsius,
                                     'pressure': f'{pressure} hPa',
                                     'humidity': f'{humidity}%',
                                     'coordinate': coordinate})

    return render_template('index.html', data=None)

@app.route('/logo')
def logo():
    return render_template('logo.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
