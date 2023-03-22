from flask import Flask, render_template, request, url_for, flash
import config
import numpy as np
import pickle
from loan_app import predictions

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods = ["POST"])
def predict():
    gender = int(request.form['gender'])
    married = int(request.form['married'])
    dependants = int(request.form['dependants'])
    education = int(request.form['education'])
    selfEmployed = int(request.form['selfEmployed'])
    amountTerm = int(request.form['amountTerm'])
    credit = int(request.form['credit'])
    parea = int(request.form['parea'])
    # Log Transforming this values as we've done the same while model building
    loanAmount = np.log(int(request.form['loanAmount']))
    totalIncome = np.log(int(request.form['totalIncome']))

    print(f"""
            Gender: {gender},
            Married: {married},
            Dependents: {dependants},
            Education: {education},
            Self Employed: {selfEmployed},
            Amount Term: {amountTerm},
            Credit: {credit},
            Parea: {parea},
            Loan Amount: {loanAmount},
            Total Income: {totalIncome}.
        """)

    data = np.array([[gender, married, dependants, education, selfEmployed, amountTerm, credit, parea, loanAmount, totalIncome]])

    result = predictions.loan_prediction(data)

    print(result)
    
    return render_template('about.html', loan_result = result)

if __name__ == "__main__":
    app.run(debug = True, host = config.HOST, port = config.PORT)