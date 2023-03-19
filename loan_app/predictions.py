from flask import flash
import pickle
import config

model = pickle.load(open(config.MODEL_PATH, 'rb'))

def loan_prediction(data):
    result = model.predict(data)

    if result[0] == 1:
        return flash('Loan Approved!', category='success')
        # return "Loan Approved!"
    else:
        return flash("Loan Declined!", category='error')