
# 🛡️ Insurance Fraud Detection

A machine learning project that gives every insurance claim a **fraud score**, so investigators can check the riskiest claims first. It includes a Jupyter notebook (model building) and a company-style **Streamlit website** (live demo).

**Live app:** _add your Streamlit link here_

---

## 📌 Problem

Insurance companies lose a lot of money to fraudulent claims, and checking every claim by hand is slow. The goal is to predict whether a claim is **fraud (Y)** or **genuine (N)** from customer, policy, accident and claim details.

## 📊 Dataset

- 1,000 auto insurance claims, 39 columns
- Target: `fraud_reported` (Y or N)
- About **25% of the claims are fraud**, so the data is moderately imbalanced
- Files: `Worksheet in Case Study question 2.xlsx` (used by the notebook) and `insurance_claims.csv` (same data, used by the app)

## 🔍 What I did

1. **Fixed hidden data problems**
   - Missing values were written as `?` in 3 columns. I kept them as an "Unknown" category, because not knowing can be a useful signal.
   - The text `"None"` in `authorities_contacted` was read as missing. I restored it.
2. **Feature engineering**
   - `policy_age_days`: days between policy start and accident
   - `vehicle_age`: age of the car at the time of the accident
3. **Removed columns that do not help:** ID-like columns (`policy_number`, `insured_zip`, `incident_location`), `auto_model` (39 values for 1,000 rows) and the original date columns.
4. **Safe preprocessing:** a scikit-learn `Pipeline` with `StandardScaler` for numbers and `OneHotEncoder` for text, so no information leaks from the test data.
5. **Compared 7 models** with 5-fold cross-validation, using class weights for the imbalance.
6. **Tuned XGBoost** with `GridSearchCV`.
7. **Chose a better decision cutoff (0.31 instead of 0.5)** using cross-validated predictions on training data only, so the model catches more frauds.

## 🏆 Results

### Model comparison (5-fold cross-validation on training data)

| Model | Recall | F1 | ROC-AUC |
|---|---|---|---|
| XGBoost | 0.818 | 0.724 | 0.858 |
| Decision Tree | 0.783 | 0.706 | 0.788 |
| Logistic Regression | 0.778 | 0.697 | 0.864 |
| Gradient Boosting | 0.672 | 0.665 | 0.856 |
| SVM | 0.652 | 0.626 | 0.822 |
| Random Forest | 0.298 | 0.395 | 0.846 |
| KNN | 0.142 | 0.207 | 0.603 |

### Final model on hidden test data (200 claims)

Tuned XGBoost with cutoff 0.31:

| Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|
| 0.845 | 0.636 | 0.857 | 0.730 | 0.836 |

- Caught **42 of 49 frauds**, missed 7
- 24 false alarms
- Strongest fraud signals: **Major Damage** claims and the hobbies **chess** and **cross-fit**

### Honest notes

- The dataset is small (only 49 frauds in the test set), so a few claims can change the scores.
- ROC-AUC is almost the same for several models, and plain Logistic Regression is close to XGBoost. Do not read small differences as real.
- The fraud score is a guide, not proof. A person should check every flagged claim.

## 🌐 Streamlit website

| Page | What it does |
|---|---|
| Home | Company-style landing page with summary numbers |
| Dashboard | Filters and 7 interactive fraud charts |
| Check a Claim | Enter one claim and get a fraud score with a verdict |
| Batch Check | Upload many claims and download a ranked report |
| Models | Model comparison and final model results |
| About | Problem, data and method |

The app works without XGBoost (it uses Random Forest instead), and shows a clear message with the exact install command if a library is missing.

## 🚀 How to run

```bash
# 1. Install libraries (use the same Python for every command)
python -m pip install -r requirements.txt

# 2. Start the website
python -m streamlit run app.py
```

It opens at `http://localhost:8501`. Keep `app.py` and `insurance_claims.csv` in the same folder.

To run the notebook, open `Insurance_Fraud_Detection.ipynb` in Jupyter or VS Code and run all cells.

### Change the name and contact details

Open `app.py`, search for `CHANGE YOUR DETAILS`, and edit `BRAND`, `CONTACT_EMAIL`, `CONTACT_PHONE`, `CONTACT_ADDRESS` and `CONTACT_LINK`.

### Common problems

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Run `python -m pip install -r requirements.txt` |
| App uses a different Python than pip | Always use `python -m pip` and `python -m streamlit` |
| Data file not found | Keep `insurance_claims.csv` next to `app.py` |

## 📁 Project structure

```
insurance_fraud_detection/
├── app.py                              # Streamlit website (single file)
├── Insurance_Fraud_Detection.ipynb     # Model building, step by step
├── insurance_claims.csv                # Data used by the app
├── Worksheet in Case Study question 2.xlsx   # Same data, used by the notebook
├── requirements.txt
├── README.md
└── .streamlit/config.toml              # Light theme for the website
```

## 🛠️ Tech stack

Python, Pandas, NumPy, Scikit-learn, XGBoost, Plotly, Streamlit, Jupyter

## 🔮 Future improvements

- Try LightGBM or CatBoost, and SMOTE on the training data only
- Collect more data, since 1,000 claims is small
- Add explanations for each score (for example SHAP)
- Deploy the app on Streamlit Community Cloud

## 👩‍💻 Author

**Anitha**
GitHub: [Anitha123-allam](https://github.com/Anitha123-allam)
LinkedIn:www.linkedin.com/in/allam-anitha-700637291
