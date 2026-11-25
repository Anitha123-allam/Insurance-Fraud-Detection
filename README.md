# Insurance Claim Fraud Detection System
<img width="1915" height="998" alt="Screenshot 2026-11-24 101759" src="https://github.com/user-attachments/assets/0804f1ef-2302-4755-b3bc-378efee3cf33" />


## 1. Project Overview

The **Insurance Claim Fraud Detection** project is a Machine Learning-based web application that predicts whether an insurance claim is potentially fraudulent or genuine based on customer details, policy information, incident characteristics, vehicle information, and claim amounts.

The application uses trained Machine Learning classification models to analyze insurance claim data and identify suspicious claims. It also provides fraud probability and risk assessment to help insurance companies prioritize claims for further investigation.

## 2. Objectives

- Detect potentially fraudulent insurance claims using Machine Learning.
- Analyze insurance claim data and identify suspicious patterns.
- Understand the relationship between claim characteristics and fraudulent activities.
- Build and compare different Machine Learning classification models.
- Predict fraud probability for insurance claims.
- Develop an interactive web application using Streamlit.

## 3. Technologies Used

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning Algorithms:** Logistic Regression, Random Forest, XGBoost
- **Web Framework:** Streamlit
- **Model Storage:** Pickle

## 4. Dataset Information

The dataset used in this project is collected from Kaggle and contains insurance claim-related information.

**Dataset Source:** [Insurance Claim Fraud Detection – Kaggle](https://www.kaggle.com/datasets/roshansharma/insurance-claim-fraud-detection)

**Important Features:**

- Customer Age
- Policy Information
- Incident Type
- Incident Severity
- Vehicle Information
- Claim Amount
- Witness Count
- Police Report Availability
- Property Damage

**Target Variable:** Fraud Reported

- **Y:** Fraudulent Claim
- **N:** Genuine Claim

## 5. Data Preprocessing

The following data preprocessing techniques are performed:

- Checked and handled missing values.
- Identified duplicate records.
- Encoded categorical variables into numerical values.
- Performed feature selection.
- Separated independent and dependent variables.
- Split the dataset into training and testing sets.
- Applied feature scaling where required.

## 6. Exploratory Data Analysis (EDA)

Performed Exploratory Data Analysis to understand the dataset and identify patterns related to insurance fraud.

- Analyzed fraudulent and genuine claim distributions.
- Examined claim amount distributions.
- Analyzed incident types and incident severity.
- Studied relationships between different features.
- Performed correlation analysis.
- Created visualizations using Matplotlib and Seaborn.

## 7. Machine Learning Models

Implemented the following classification algorithms:

- **Logistic Regression:** Used as a baseline classification model.
- **Random Forest Classifier:** Used multiple decision trees to classify insurance claims.
- **XGBoost Classifier:** Applied gradient boosting for fraud classification.

The models are compared using different evaluation metrics to identify the most suitable model.

## 8. Model Evaluation

Evaluated model performance using the following metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

Recall and F1-score are particularly important for identifying fraudulent claims and reducing missed fraud cases.

## 9. Streamlit Web Application

Developed an interactive web application using Streamlit to predict potentially fraudulent insurance claims.

**Application Features:**

- Enter insurance claim details.
- Predict fraudulent or genuine claims.
- Display fraud probability.
- Classify claims into High, Medium, and Low risk levels.
- Provide investigation recommendations.
- Generate real-time predictions.

**Sample Output:**

```text
Fraud Probability : 87%

Risk Level : HIGH

Recommendation : Manual Investigation Required
```

## 10. Business Benefits

- Helps identify suspicious insurance claims.
- Reduces the risk of fraudulent payouts.
- Improves claim investigation efficiency.
- Saves operational time and costs.
- Supports data-driven decision-making.
- Helps insurance companies prioritize suspicious claims.

## 11. Future Enhancements

- Implement SHAP for model explainability.
- Develop an interactive fraud analytics dashboard.
- Add document verification functionality.
- Perform hyperparameter tuning.
- Improve model performance.
- Deploy the application on a cloud platform.

## 12. Conclusion

This project demonstrates the application of Machine Learning in solving real-world insurance fraud detection problems.

By analyzing insurance claim information and identifying potentially fraudulent activities, the system helps insurance companies improve investigation efficiency, reduce financial risks, and make better data-driven decisions.

---

**Project Domain:** Data Science and Machine Learning

**Project Type:** Binary Classification

**Algorithms:** Logistic Regression, Random Forest, XGBoost

**Deployment:** Streamlit Web Application
