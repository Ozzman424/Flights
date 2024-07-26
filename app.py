from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_KEY = 'your_skyscanner_api_key'  # Replace with your Skyscanner API key

def find_flights(origin, destination, date):
    url = f"https://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/US/USD/en-US/{origin}/{destination}/{date}"
    params = {
        'apikey': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        origin = request.form['origin']
        destination = request.form['destination']
        date = request.form['date']
        flights = find_flights(origin, destination, date)
        return render_template('index.html', flights=flights)
    return render_template('index.html', flights=None)

if __name__ == "__main__":
    app.run(debug=True)
