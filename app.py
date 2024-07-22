import os
from flask import Flask, render_template, request
from capm_analysis import calculate_capm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/capm', methods=['POST'])
def capm():
    risk_free_rate = float(request.form['risk_free_rate'])
    beta = float(request.form['beta'])
    market_return = float(request.form['market_return'])
    expected_return = calculate_capm(risk_free_rate, beta, market_return)
    return render_template('index.html', result=expected_return)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))

