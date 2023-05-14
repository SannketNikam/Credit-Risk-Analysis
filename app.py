from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from os import path
import config
import numpy as np
from loan_app import predictions

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///credito.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "secret key"
db = SQLAlchemy(app)

# Loan Approval Page Table
class LoanApproval(db.Model):
    sno = db.Column(db.Integer, primary_key = True, autoincrement = True)
    firstName = db.Column(db.String(50), nullable = True)
    lastName = db.Column(db.String(50), nullable = True)
    gender = db.Column(db.String(10), nullable = True)
    married = db.Column(db.String(10), nullable = True)
    education = db.Column(db.String(10), nullable = True)
    selfEmployed = db.Column(db.String(10), nullable = True)
    credit = db.Column(db.String(10), nullable = True)
    parea = db.Column(db.String(50), nullable = True)
    dependants = db.Column(db.String(10), nullable = True)
    totalIncome = db.Column(db.String(50), nullable = True)
    amountTerm = db.Column(db.String(50), nullable = True)
    loanAmount = db.Column(db.String(50), nullable = True)
    approval = db.Column(db.String(10), nullable = True)

    def __repr__(self) -> str:
        return f"""
        First Name: {self.firstName} -
        Last Name: {self.lastName} - 
        Gender: {self.gender} - 
        Married: {self.married} - 
        Education: {self.education} - 
        Self Employed: {self.selfEmployed} - 
        Credit: {self.credit} - 
        parea: {self.parea} - 
        Dependants: {self.dependants} - 
        Total Income: {self.totalIncome} - 
        Loan Term: {self.amountTerm} - 
        Loan Amount: {self.loanAmount}
        Approval: {self.approval}."""

# Contact Page Table
class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key = True, autoincrement = True)
    fullname = db.Column(db.String(50), nullable = True)
    email = db.Column(db.String(50), nullable = True)
    phone = db.Column(db.Integer, nullable = True)
    subject = db.Column(db.String(50), nullable = True)
    message = db.Column(db.Text, nullable = True)

    def __repr__(self) -> str:
        return f"""
        FullName: {self.fullname} -
        Email: {self.email} - 
        Phone: {self.phone} - 
        Subject: {self.subject} -
        Message: {self.message}."""
    
@app.route('/', methods = ["GET", "POST"])
def index():
    return render_template('home.html')

@app.route('/loan-approval')
def predict():
    return render_template("loan-approval.html")

@app.route('/about', methods = ["GET", "POST"])
def about():
    if request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        gender = request.form["gender"]
        married = request.form["married"]
        dependants = request.form["dependants"]
        education = request.form["education"]
        selfEmployed = request.form["selfEmployed"]
        amountTerm = request.form["amountTerm"]
        credit = request.form["credit"]
        parea = request.form["parea"]
        loanAmount = request.form["loanAmount"]
        totalIncome = request.form["totalIncome"]

        gender = int(gender)
        married = int(married)
        dependants = int(dependants)
        education = int(education)
        selfEmployed = int(selfEmployed)
        amountTerm = int(amountTerm)
        credit = int(credit)
        parea = int(parea)
        # Log Transforming this values as we've done the same while model building
        loanAmount = np.log(int(loanAmount))
        totalIncome = np.log(int(totalIncome))
        
        print(f"""
            Gender: {gender},
            Married: {married},
            Dependants: {dependants},
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

        # Adding new data to database
        loanapproval = LoanApproval(firstName = firstName, lastName = lastName, gender = gender, married = married, dependants = dependants, education = education, selfEmployed = selfEmployed, amountTerm = amountTerm, credit = credit, parea = parea, loanAmount = loanAmount, totalIncome = totalIncome)
        db.session.add(loanapproval)
        db.session.commit()
        
        return render_template('about.html', loan_result = result)
    
    else:
        return render_template('about.html')

@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        phone = request.form["phone"]
        subject = request.form["subject"]
        message = request.form["message"]
        contact = Contact(fullname = fullname, email = email, phone = phone, subject = subject, message = message)
        db.session.add(contact)
        db.session.commit()

    allContact = Contact.query.all()
    return render_template('contact.html', allContact = allContact)

@app.route('/navigation-mobile')
def navigation_mobile():
    return render_template('navigation-mobile.html')

@app.route('/loan-approval', methods = ["GET", "POST"])
def loan_approval():
    if request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        gender = request.form["gender"]
        married = request.form["married"]
        dependants = request.form["dependants"]
        education = request.form["education"]
        selfEmployed = request.form["selfEmployed"]
        amountTerm = request.form["amountTerm"]
        credit = request.form["credit"]
        parea = request.form["parea"]
        loanAmount = request.form["loanAmount"]
        totalIncome = request.form["totalIncome"]

        gender = int(gender)
        married = int(married)
        dependants = int(dependants)
        education = int(education)
        selfEmployed = int(selfEmployed)
        amountTerm = int(amountTerm)
        credit = int(credit)
        parea = int(parea)
        # Log Transforming this values as we've done the same while model building
        loanAmount = np.log(int(loanAmount))
        totalIncome = np.log(int(totalIncome))
        
        print(f"""
            Gender: {gender},
            Married: {married},
            Dependants: {dependants},
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
    
    else:
        return render_template("loan-approval.html")

# To delete all records from the database
@app.route("/delete")
def delete():
    db.session.query(Contact).delete()
    db.session.query(LoanApproval).delete()
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":

    if not path.exists("./instance/credito.db"):
        app.app_context().push()
        db.create_all()
    else:
        pass

# While deploying turn debug to false
    app.run(debug = False, host = config.HOST, port = config.PORT)