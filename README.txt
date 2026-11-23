🛡️ Insurance Claim Fraud Detection System
📌 Project Overview
Insurance fraud is a major challenge for insurance companies, leading to significant financial losses every year. This project uses Machine Learning techniques to identify potentially fraudulent insurance claims and assist investigators in prioritizing suspicious cases.

The system analyzes claim-related information such as customer details, incident characteristics, claim amount, vehicle information, and policy details to predict whether a claim is likely to be fraudulent.

🎯 Problem Statement
Insurance companies process thousands of claims every day. Manually reviewing every claim is time-consuming and expensive.

The objective of this project is to build a Machine Learning model that can:

Detect fraudulent claims
Reduce financial losses
Improve claim investigation efficiency
Support decision-making using predictive analytics
📊 Dataset
Dataset Source:

https://www.kaggle.com/datasets/roshansharma/insurance-claim-fraud-detection

Features Included
Customer Age
Policy Information
Incident Type
Incident Severity
Vehicle Information
Claim Amount
Witness Count
Police Report Availability
Property Damage Information
Target Variable
Fraud Reported

Y → Fraudulent Claim
N → Genuine Claim
⚙️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn
Streamlit
🔄 Project Workflow
1. Data Collection
Load insurance claim dataset.

2. Data Preprocessing
Handle missing values
Remove duplicates
Encode categorical variables
Feature selection
3. Exploratory Data Analysis (EDA)
Fraud distribution analysis
Claim amount analysis
Incident severity analysis
Feature correlation analysis
4. Model Building
Machine Learning Algorithms:

Logistic Regression
Random Forest Classifier
XGBoost Classifier
5. Model Evaluation
Evaluation Metrics:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix
6. Deployment
Deploy the trained model using Streamlit.

🚀 Application Features
✅ Predict Insurance Fraud

✅ Fraud Probability Score

✅ Real-Time Predictions

✅ User-Friendly Interface

✅ Risk Assessment Recommendations

💻 Streamlit Application
Users can enter:

Customer Age
Claim Amount
Vehicle Age
Incident Severity
Witness Count
Police Report Status
The application predicts:

Fraud Risk: High / Medium / Low

Fraud Probability: XX%
📈 Business Benefits
Detect suspicious claims earlier
Reduce fraudulent payouts
Improve investigation efficiency
Save operational costs
Minimize financial losses
📷 Sample Output
Fraud Probability : 87%

Risk Level : HIGH

Recommendation :
Manual Investigation Required
📁 Project Structure
Insurance-Fraud-Detection/
│
├── dataset/
│   └── insurance_claims.csv
│
├── notebooks/
│   └── Insurance_Fraud_Detection.ipynb
│
├── models/
│   └── fraud_model.pkl
│
├── app/
│   └── streamlit_app.py
│
├── requirements.txt
│
└── README.md
Future Enhancements
SHAP Explainability
Fraud Analytics Dashboard
Document Verification Module
Multiple Model Comparison
Cloud Deployment
Conclusion
This project demonstrates the application of Machine Learning for fraud detection in the insurance industry. By automating fraud identification, insurance companies can reduce risks, improve operational efficiency, and make data-driven claim investigation decisions.
