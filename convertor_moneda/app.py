from flask import Flask, render_template, request  
import requests  

app = Flask(__name__)  

@app.route('/', methods=['GET', 'POST'])  
def index():  
    conversion_result = None  
    error_message = None  
    if request.method == 'POST':  
        amount = request.form.get('amount')  
        from_currency = request.form.get('from_currency').upper()  
        to_currency = request.form.get('to_currency').upper()  
        
        try:  
            amount = float(amount)  
            if amount <= 0:  
                error_message = "La cantidad debe ser un número positivo."  
            else:  
                conversion_result, error_message = convert_currency(amount, from_currency, to_currency)  
        except ValueError:  
            error_message = "Por favor, introduce un número válido para la cantidad."  

    return render_template('index.html', conversion_result=conversion_result, error_message=error_message)  

# def convert_currency(amount, from_currency, to_currency):  
#     api_key = 'deffc8e0f02d5e805e0d2e6'  # Asegúrate de no compartir tu API key  
#     url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'  
#     response = requests.get(url)  
def convert_currency(amount, from_currency, to_currency):  
    print(f"Convirtiendo {amount} de {from_currency} a {to_currency}")  # Agrega esta línea  
    api_key = 'deffc8e0f02d5e805e0d2e6'  
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'  
    response = requests.get(url)  
    print(f"Respuesta {response.status_code}: {response.text}")  # Agrega esta línea para ver la respuesta  
    
    if response.status_code != 200:  
        return None, "Error en la conversión. Verifica la moneda o intenta nuevamente más tarde."  

    data = response.json()  

    if 'error' in data:  
        return None, data['error-type']  

    if to_currency not in data['rates']:  
        return None, f"Moneda '{to_currency}' no encontrada."  

    rate = data['rates'][to_currency]  
    converted_amount = round(amount * rate, 2)  
    return converted_amount, None  

if __name__ == '__main__':  
    app.run(debug=True)