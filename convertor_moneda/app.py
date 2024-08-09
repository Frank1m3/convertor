from flask import Flask, render_template, request
import requests 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    conversion_result = None
    if request.method == 'POST':
        amount = request.form.get('amount')
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        conversion_result = convert_currency(amount, from_currency, to_currency)
    return render_template('index.html', conversion_result=conversion_result)

def convert_currency(amount, from_currency, to_currency):
    api_key ='deffc8e0f02d5e805e0d2e6'
    url = f'https://v6.exchangerate-api.com/v6/deffc8e0f02d5e8a05e0d2e6/latest/USD{from_currency}'
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    return float(amount) * rate

if __name__ == '__main__':
    app.run(debug=True)
