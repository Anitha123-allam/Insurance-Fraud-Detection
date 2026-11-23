# 🛡️ Insurance Claim Fraud Detection System Using Machine Learning

## 📌 Project Overview

Insurance fraud is one of the major challenges faced by insurance companies, resulting in significant financial losses. Detecting fraudulent claims manually is time-consuming and requires significant effort.

This project aims to develop a Machine Learning-based Insurance Claim Fraud Detection System that identifies potentially fraudulent insurance claims based on customer details, policy information, incident characteristics, vehicle details, and claim amounts.

The system uses classification algorithms to predict whether an insurance claim is **Fraudulent or Genuine** and helps insurance companies identify suspicious claims for further investigation.

## 🎯 Problem Statement

Insurance companies receive thousands of claims, making manual fraud detection difficult and expensive.

The objective of this project is to build a predictive model that:

- Identifies potentially fraudulent insurance claims.
- Analyzes claim-related information.
- Calculates fraud probability.
- Helps prioritize suspicious claims.
- Improves claim investigation efficiency.

## 📊 Dataset Information

**Dataset:** Insurance Claim Fraud Detection

**Source:** [Kaggle – Insurance Claim Fraud Detection](https://www.kaggle.com/datasets/roshansharma/insurance-claim-fraud-detection)

The dataset contains insurance claim information, including customer details, policy details, incident information, and claim amounts.

### Important Features

- Customer Age
- Policy Number
- Policy Annual Premium
- Incident Type
- Incident Severity
- Vehicle Age
- Vehicle Information
- Total Claim Amount
- Witness Count
- Police Report Availability
- Property Damage

### Target Variable

`Fraud Reported`

- **Y** – Fraudulent Claim
- **N** – Genuine Claim

## 🛠️ Technologies & Tools Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning |
| XGBoost | Gradient boosting |
| Streamlit | Web application |
| Pickle | Model serialization |

## 🔄 Project Workflow

### 1. Data Collection
- Imported the insurance claim dataset.
- Explored dataset structure and feature information.

### 2. Data Preprocessing
- Checked and handled missing values.
- Removed duplicate records.
- Encoded categorical variables.
- Prepared features for model training.

### 3. Exploratory Data Analysis (EDA)
- Analyzed fraudulent and genuine claim distributions.
- Studied claim amounts and incident severity.
- Explored relationships between customer, policy, and incident features.
- Identified important patterns associated with fraudulent claims.

### 4. Model Building

Implemented and compared the following classification algorithms:

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

### 5. Model Evaluation

Evaluated model performance using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Recall and F1-score are particularly important because identifying fraudulent claims while minimizing missed fraud cases is a key objective.

### 6. Model Deployment

Developed an interactive Streamlit application that allows users to enter insurance claim information and receive fraud predictions.

## 🚀 Application Features

- Insurance Claim Fraud Prediction
- Fraud Probability Score
- Real-Time Prediction
- High, Medium, and Low Risk Classification
- Interactive User Interface
- Investigation Recommendations

## 💻 Streamlit Application

Users can enter claim-related details such as:

- Customer Age
- Claim Amount
- Vehicle Age
- Incident Severity
- Witness Count
- Police Report Status

The application generates a prediction containing:

**Sample Output:**

```text
Fraud Probability: 87%

Risk Level: HIGH

Prediction: Potentially Fraudulent

Recommendation: Manual Investigation Required
```

*Sample output for illustration only.*

## 📁 Project Structure

```text
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
```

## 📈 Business Benefits

- Helps identify suspicious insurance claims.
- Reduces the possibility of fraudulent payouts.
- Saves time in claim investigation.
- Improves operational efficiency.
- Supports data-driven decision-making.
- Helps prioritize high-risk insurance claims.

## 🔮 Future Enhancements

- Implement SHAP for model explainability.
- Develop an interactive fraud analytics dashboard.
- Add document verification functionality.
- Improve model performance through hyperparameter tuning.
- Deploy the application on a cloud platform.

## 🏁 Conclusion

The Insurance Claim Fraud Detection System demonstrates how Machine Learning can be applied to solve a real-world problem in the insurance industry.

By analyzing claim information and predicting potentially fraudulent activities, this system can help insurance companies improve fraud investigation, reduce financial risks, and make more informed decisions.

---

**Project Domain:** Machine Learning | Data Science | Insurance Analytics

**Project Type:** Binary Classification

**Application:** Streamlit Web Application
