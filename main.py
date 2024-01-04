from flask import Flask, render_template, request
from datetime import date
import requests

app = Flask(__name__)

BASE_URL= "https://api.nasa.gov/planetary/apod"

try:
    import config
    API_KEY = config.API_KEY
except ImportError:
    API_KEY = "DEMO_KEY"
    print("using DEMO_KEY")


@app.route('/', methods=['GET', 'POST'])
def home():
    today = str(date.today())
    if request.method == 'GET':
        data = get_nasa_apod(today)
        return render_template('index.html', data=[data], today=today)

    if request.form['date']:
        data = get_nasa_apod(request.form['date'])
        return render_template('index.html', data=[data], today=today, day=request.form['date'])
    else:
        return render_template('index.html')

def get_nasa_apod(date):
    url = f"{BASE_URL}?api_key={API_KEY}&date={date}"
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)

