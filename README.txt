
# 🛡️ Insurance Claim Fraud Detection System

### Machine Learning | Classification | Python | Streamlit

---

## 📌 Project Overview

Insurance fraud is one of the major challenges in the insurance industry, resulting in significant financial losses. Identifying fraudulent claims manually is time-consuming and requires considerable effort.

The **Insurance Claim Fraud Detection System** is a Machine Learning-based project designed to identify potentially fraudulent insurance claims by analyzing customer details, policy information, incident characteristics, vehicle information, and claim amounts.

This project applies classification algorithms to predict whether an insurance claim is fraudulent or genuine. It also provides fraud probability and risk assessment to help prioritize suspicious claims for further investigation.

## 🎯 Problem Statement

Insurance companies process thousands of claims regularly. Manually reviewing every claim makes fraud detection difficult, expensive, and time-consuming.

The objective of this project is to develop a predictive system that analyzes insurance claim data and identifies potentially fraudulent activities.

### Project Objectives

- Identify potentially fraudulent insurance claims.
- Analyze patterns in insurance claim data.
- Understand factors associated with fraudulent claims.
- Build and compare multiple Machine Learning models.
- Predict fraud probability for new insurance claims.
- Support efficient claim investigation and decision-making.

---

## 📊 Dataset Description

**Dataset Source:** [Insurance Claim Fraud Detection – Kaggle](https://www.kaggle.com/datasets/roshansharma/insurance-claim-fraud-detection)

The dataset contains information about customers, insurance policies, incidents, vehicles, and claim details.

### Important Features

| Feature | Description |
|---|---|
| Age | Customer age |
| Policy Information | Insurance policy details |
| Incident Type | Type of insurance incident |
| Incident Severity | Severity of the incident |
| Vehicle Age | Age of the insured vehicle |
| Total Claim Amount | Total amount claimed |
| Witnesses | Number of witnesses |
| Police Report | Availability of police report |
| Property Damage | Property damage information |

### Target Variable

**Fraud Reported**

- `Y` – Fraudulent Claim
- `N` – Genuine Claim

---

## 🔍 Exploratory Data Analysis (EDA)

Performed Exploratory Data Analysis to understand the dataset, discover patterns, and identify relationships between different features.

Key analysis performed:

- Dataset structure and statistical summary.
- Missing value analysis.
- Duplicate record analysis.
- Fraudulent vs. genuine claim distribution.
- Claim amount distribution.
- Incident severity analysis.
- Categorical feature analysis.
- Correlation analysis.
- Data visualization using Matplotlib and Seaborn.

---

## ⚙️ Data Preprocessing

The following preprocessing techniques were applied:

- Handled missing values.
- Checked and removed duplicate records where applicable.
- Encoded categorical variables into numerical values.
- Selected relevant features for model training.
- Separated independent and dependent variables.
- Split the dataset into training and testing sets.
- Applied feature scaling where required.

---

## 🤖 Machine Learning Models

Implemented and compared the following classification algorithms:

| Algorithm | Description |
|---|---|
| Logistic Regression | Used as a baseline classification algorithm. |
| Random Forest Classifier | Uses multiple decision trees to improve prediction performance. |
| XGBoost Classifier | Uses gradient boosting to improve classification performance. |

The models are compared to identify the most suitable algorithm for insurance fraud detection.

---

## 📈 Model Evaluation

Model performance is evaluated using the following metrics:

- **Accuracy:** Measures the overall percentage of correct predictions.
- **Precision:** Measures how many predicted fraudulent claims are actually fraudulent.
- **Recall:** Measures how many actual fraudulent claims are correctly identified.
- **F1-Score:** Provides a balance between precision and recall.
- **Confusion Matrix:** Shows correct and incorrect classifications.

Recall and F1-score are particularly important because failing to identify fraudulent claims can lead to financial losses.

---

## 🚀 Streamlit Web Application

Developed an interactive web application using Streamlit to make fraud prediction easier.

### Application Features

- Enter insurance claim details.
- Predict whether a claim is potentially fraudulent or genuine.
- Display fraud probability.
- Classify claims into High, Medium, and Low risk categories.
- Provide investigation recommendations.
- Generate real-time predictions.

### Sample Prediction

```text
Prediction       : Potentially Fraudulent
Fraud Probability: 87%
Risk Level       : HIGH

Recommendation:
Manual Investigation Required
```

*Illustrative output only.*

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data Manipulation |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Scikit-learn | Machine Learning |
| XGBoost | Gradient Boosting |
| Streamlit | Application Development |
| Pickle | Model Saving |

---

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

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Insurance-Fraud-Detection.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Insurance-Fraud-Detection
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
streamlit run app/streamlit_app.py
```

---

## 💡 Business Benefits

- Helps identify suspicious insurance claims.
- Reduces the possibility of fraudulent payouts.
- Improves claim investigation efficiency.
- Saves operational time and costs.
- Supports data-driven business decisions.
- Helps prioritize claims requiring further investigation.

---

## 🔮 Future Enhancements

- Implement SHAP for model explainability.
- Develop an interactive fraud analytics dashboard.
- Add document verification functionality.
- Perform hyperparameter tuning.
- Improve prediction performance.
- Deploy the application on a cloud platform.

---

## 🏁 Conclusion

The Insurance Claim Fraud Detection System demonstrates the practical application of Machine Learning in solving real-world insurance industry problems.

By analyzing insurance claim data and identifying potentially fraudulent activities, the system can support insurance companies in prioritizing suspicious claims, improving investigation efficiency, and reducing financial risks.

---

### 👩‍💻 Project Information

**Project Name:** Insurance Claim Fraud Detection System

**Domain:** Data Science & Machine Learning

**Problem Type:** Binary Classification

**Algorithms:** Logistic Regression, Random Forest, XGBoost

**Deployment:** Streamlit

**Dataset:** Kaggle – Insurance Claim Fraud Detection
