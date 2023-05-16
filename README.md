# 🏦Credit Risk Analysis💸

<img src="./static/images/Home_page_mobile.png"/>

## What is Credit Risk Analysis?
**Credit Risk Analysis** is an important process that enables lenders, credit rating agencies, and other financial institutions to evaluate the creditworthiness of borrowers and make informed decisions about extending credit. In this project, we will be using the **XGBoost** algorithm to predict whether a borrower is likely to default on a loan or not.

## Dataset
The <a href="./Data/">dataset</a> used in this project contains information about the loan issued including the Loan ID, Gender, Married, Dependents, Education, Self Employed, Applicant Income, Co-Applicant Income, Loan Amount, Loan Amount Term, Credit History, Property Area and Loan Status.

## Preprocessing
Before building our XGBoost model, the data was preprocessed by handling missing values, converting categorical variables to numerical and Label Encoding some features.

## Model Building
We will be using XGBoost, a popular gradient boosting algorithm, to predict the likelihood of loan default. We will train the model on the preprocessed data and evaluate its performance using metrics such as accuracy, precision, recall, and F1-score.

## Results
Our XGBoost model achieves an accuracy of 85% indicating that it is a good predictor of loan default.

## Conclusion
In this project, we have demonstrated the use of XGBoost for credit risk analysis. By training a model on the loan dataset, we were able to predict the likelihood of loan default with high accuracy. This type of analysis can be useful for lenders and other financial institutions to make informed decisions about extending credit to borrowers.

# Loan Approval Page:
<img src="./static/images/Loan Approval.png"/>

# Installation:
1. Clone the repository to your local machine:
```
git clone https://github.com/SannketNikam/Credit-Risk-Analysis.git
```

2. Install the 'requirements.txt':
```
pip install -r requirements.txt
```

3. To run this project :
```
python app.py
```

4. Visit your browser at:
```
http://127.0.0.1:8080
```
