from flask import Flask, jsonify, request

app = Flask(__name__)

# Taxas simuladas
exchange_rates = {
    'USD': 1.00,
    'EUR': 0.92,
    'BRL': 5.10
}

def convert_to_float(value):
    if isinstance(value, str):
        value = value.replace(',', '.')
    try:
        return float(value)
    except:
        return None

def validate(amount, from_c, to_c):
    missing = [k for k, v in {
        'amount': amount,
        'from': from_c,
        'to': to_c
    }.items() if v is None]

    if missing:
        return {'error': 'Missing parameters', 'parameters_missing': missing}, 400

    amount_f = convert_to_float(amount)
    if amount_f is None:
        return {'error': 'Invalid amount'}, 400

    from_c = from_c.upper()
    to_c = to_c.upper()

    if from_c not in exchange_rates or to_c not in exchange_rates:
        return {'error': 'Currency not supported'}, 400

    return None, amount_f, from_c, to_c

@app.route('/convert')
def convert():
    amount = request.args.get('amount')
    from_c = request.args.get('from')
    to_c = request.args.get('to')

    error, *rest = validate(amount, from_c, to_c)
    if error:
        return jsonify(error), rest[0]

    amount_f, from_c, to_c = rest
    rate = exchange_rates[to_c] / exchange_rates[from_c]
    converted = round(amount_f * rate, 2)

    return jsonify({
        'amount': amount_f,
        'from': from_c,
        'to': to_c,
        'converted_amount': converted
    })

if __name__ == '__main__':
    app.run(debug=True)
