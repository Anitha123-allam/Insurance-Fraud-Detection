🛡️ Insurance Claim Fraud Detection Using Machine Learning

📌 Project Overview

Insurance fraud is a major challenge for insurance companies, leading to financial losses. Manually checking every insurance claim is time-consuming and difficult.

This project uses Machine Learning to identify potentially fraudulent insurance claims and distinguish between Fraudulent (Y) and Genuine (N) claims.

The system analyzes customer information, policy details, accident characteristics, and claim amounts to predict the probability of fraud and help investigators prioritize suspicious claims.

🎯 Project Objectives

Identify potentially fraudulent insurance claims.

Perform Exploratory Data Analysis (EDA) to discover fraud patterns.

Compare multiple Machine Learning classification algorithms.

Improve model performance using hyperparameter tuning.

Predict the probability of insurance claim fraud.

Help insurance investigators focus on high-risk claims.

📂 Dataset Information

Dataset: Insurance Claims Dataset

Total Records: 1,000

Target Variable: fraud_reported

Prediction Classes:

Y – Fraudulent claim

N – Genuine claim

The dataset contains information about:

Customer details

Insurance policy information

Incident and accident details

Vehicle information

Insurance claim amounts

Fraud reporting status

🛠️ Technologies Used

Python

Jupyter Notebook

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

XGBoost

Joblib

🔍 Project Workflow

1. Data Loading and Understanding

Imported the dataset using Pandas.

Checked dataset dimensions, data types and structure.

Identified numerical and categorical columns.

2. Data Cleaning

Identified missing values and duplicate records.

Handled hidden missing values represented by ?.

Replaced unknown values with the category Unknown.

Restored None values in the authorities_contacted column.

3. Exploratory Data Analysis (EDA)

Analyzed fraud and genuine claim distribution.

Studied fraud rates based on incident severity.

Analyzed fraud patterns based on insured hobbies.

Compared claim amounts between fraud and genuine claims.

Performed correlation analysis.

4. Feature Engineering

Created two new features:

policy_age_days – Number of days between policy binding and the accident.

vehicle_age – Age of the vehicle at the time of the incident.

Removed unnecessary and ID-like columns to improve model performance.

5. Data Preprocessing

Applied StandardScaler for numerical features.

Applied OneHotEncoder for categorical features.

Used ColumnTransformer and Pipeline.

Split the dataset into 80% training and 20% testing data.

Used stratified sampling to maintain class distribution.

6. Machine Learning Model Comparison

Implemented and compared seven classification algorithms:

Algorithm

Purpose

Logistic Regression

Baseline classification

K-Nearest Neighbors (KNN)

Similarity-based classification

Support Vector Machine (SVM)

Classification using decision boundaries

Decision Tree

Rule-based classification

Random Forest

Ensemble learning using multiple trees

Gradient Boosting

Sequential boosting algorithm

XGBoost

Advanced gradient boosting algorithm

Used 5-Fold Stratified Cross-Validation to compare model performance.

7. Model Evaluation

Evaluated models using:

Accuracy

Precision

Recall

F1-Score

ROC-AUC Score

Confusion Matrix

8. Hyperparameter Tuning

Selected XGBoost for further optimization.

Used GridSearchCV to tune:

Number of estimators

Maximum tree depth

Learning rate

9. Threshold Optimization

Generated cross-validated predictions on training data.

Compared precision, recall and F1-score at different thresholds.

Selected a threshold that maximizes F1-score.

Used the optimized threshold for final fraud classification.

10. Final Prediction

Evaluated the final model on unseen test data.

Analyzed the confusion matrix and classification report.

Identified important features influencing fraud predictions.

Saved the trained model using Joblib.

📊 Key Insights

Approximately 25% of claims in the dataset are fraudulent.

Major Damage incidents show a higher fraud rate.

Chess and Cross-fit hobbies show higher fraud rates in this dataset.

Incident severity and insured hobbies are among the important model features.

XGBoost was selected for hyperparameter tuning and further evaluation.

📁 Project Structure

Insurance-Fraud-Detection/
│
├── Insurance_Fraud_Detection.ipynb
├── Worksheet in Case Study question 2.csv
├── fraud_model.pkl
├── requirements.txt
└── README.md

⚙️ Installation and Execution

Step 1: Clone the repository

git clone https://github.com/your-username/Insurance-Fraud-Detection.git

Step 2: Navigate to the project folder

cd Insurance-Fraud-Detection

Step 3: Install required libraries

pip install -r requirements.txt

Step 4: Open Jupyter Notebook

jupyter notebook

Step 5: Open Insurance_Fraud_Detection.ipynb and run the cells sequentially.

Keep the dataset CSV file in the same folder as the notebook.

💾 Model Deployment Preparation

The trained preprocessing and XGBoost pipeline is saved as:

fraud_model.pkl

The saved file includes:

Trained XGBoost model

Selected classification threshold

Required input column names

A prediction function accepts a new insurance claim and returns:

Fraud prediction

Estimated fraud probability

🚀 Future Enhancements

Develop an interactive Streamlit web application.

Integrate real-time insurance claim prediction.

Explore advanced algorithms such as LightGBM and CatBoost.

Apply SMOTE to address class imbalance.

Train using a larger insurance claims dataset.

Create an interactive dashboard for fraud analytics.

👩‍💻 Author

Anitha Allam

Aspiring Data Analyst | Machine Learning Enthusiast
