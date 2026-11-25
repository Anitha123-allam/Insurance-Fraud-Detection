
# Insurance Claim Fraud Detection System

## 1. Project Overview

The **Insurance Claim Fraud Detection** project is a Machine Learning-based application that identifies potentially fraudulent insurance claims based on customer details, policy information, incident characteristics, vehicle information, and claim amounts.

The application uses Machine Learning classification algorithms to predict whether an insurance claim is fraudulent or genuine. It helps identify suspicious claims and supports insurance companies in improving their claim investigation process.

## 2. Objectives

- Detect potentially fraudulent insurance claims using Machine Learning.
- Analyze insurance claim information and identify fraud patterns.
- Understand the relationship between claim characteristics and fraudulent activities.
- Build and compare different classification models.
- Predict fraud probability for new insurance claims.
- Develop an interactive web application using Streamlit.

## 3. Technologies Used

- **Programming Language:** Python
- **Libraries:** NumPy, Pandas, Scikit-learn
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Logistic Regression, Random Forest, XGBoost
- **Web Framework:** Streamlit
- **Model Storage:** Pickle

## 4. Dataset Information

The dataset is collected from Kaggle and contains insurance claim-related information.

**Dataset Source:** [Insurance Claim Fraud Detection - Kaggle](https://www.kaggle.com/datasets/roshansharma/insurance-claim-fraud-detection)

**Important Features:**

- Customer Age
- Policy Information
- Incident Type
- Incident Severity
- Vehicle Age
- Total Claim Amount
- Witness Count
- Police Report Availability
- Property Damage

**Target Variable:** Fraud Reported

- **Y:** Fraudulent Claim
- **N:** Genuine Claim

## 5. Data Preprocessing

The following preprocessing techniques are performed:

- Checked and handled missing values.
- Identified duplicate records.
- Converted categorical variables into numerical values.
- Performed feature selection.
- Separated independent and dependent variables.
- Split the dataset into training and testing sets.
- Applied feature scaling where required.

## 6. Exploratory Data Analysis (EDA)

Performed Exploratory Data Analysis to understand the dataset and identify patterns related to insurance fraud.

- Analyzed fraudulent and genuine claim distribution.
- Examined claim amount distribution.
- Analyzed incident types and severity.
- Studied relationships between different features.
- Performed correlation analysis.
- Created visualizations using Matplotlib and Seaborn.

## 7. Machine Learning Models

Implemented the following classification algorithms:

- **Logistic Regression:** Used as a baseline classification model.
- **Random Forest Classifier:** Used an ensemble of decision trees for fraud classification.
- **XGBoost Classifier:** Applied gradient boosting to improve classification performance.

Compared the models using different evaluation metrics to identify the most suitable model.

## 8. Model Evaluation

Evaluated the classification models using the following metrics:

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

By analyzing insurance claim information and identifying potentially fraudulent activities, the system helps insurance companies improve investigation efficiency, reduce financial risks, and support better decision-making.
