from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def rate():
    url = "https://gaialens-esg-scores.p.rapidapi.com/scores"

    querystring = {"companyname": request.form.get('input')}

    headers = {
        "X-RapidAPI-Key": "192df996a9mshd602acc52d5696dp1ff0dajsn8d04d7cc8b87",
        "X-RapidAPI-Host": "gaialens-esg-scores.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    print(data)

    return data

@app.route('/')
def index():
    return render_template('index.html')