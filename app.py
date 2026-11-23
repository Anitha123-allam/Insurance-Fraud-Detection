# ============================================================
#  FraudShield AI - Company-style website (Streamlit)
#  Run with:  streamlit run app.py
#  Files needed in the same folder:
#     app.py, images_svg.py, requirements.txt,
#     Worksheet in Case Study question 2.xlsx, .streamlit/config.toml
# ============================================================
import base64
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score,
                             precision_recall_curve, precision_score,
                             recall_score, roc_auc_score, roc_curve)
from sklearn.model_selection import (StratifiedKFold, cross_val_predict,
                                     cross_validate, train_test_split)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

try:
    from xgboost import XGBClassifier
except ModuleNotFoundError as error:
    if error.name != "xgboost":
        raise
    XGBClassifier = None

import images_svg as art          # our drawn illustrations

ROOT = Path(__file__).resolve().parent
FILE = ROOT / "Worksheet in Case Study question 2.csv"
BRAND = "FraudShield"
FINAL_MODEL_NAME = "XGBoost" if XGBClassifier is not None else "Gradient Boosting (fallback)"
MODEL_COMPARISON_COUNT = 7 if XGBClassifier is not None else 6

st.set_page_config(page_title="FraudShield AI", page_icon="🛡️", layout="wide",
                   initial_sidebar_state="collapsed")

# ---------- 1. STYLE (CSS) : makes Streamlit look like a company website ----------
CSS = """
<style>
/* hide Streamlit's own menu, header, footer and sidebar */
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stSidebar"],
[data-testid="collapsedControl"], [data-testid="stSidebarCollapsedControl"] { display: none !important; }
.stApp { background: #f6f8fc; }
.block-container { padding: 96px 2.2rem 0 2.2rem !important; max-width: 1240px; }
.stApp, .stApp p, .stApp li, .stApp label { color: #1b2559; }
h1, h2, h3, h4 { color: #1b2559; font-weight: 800; letter-spacing: -0.5px; }

/* ----- top navigation bar ----- */
.navbar { position: fixed; top: 0; left: 0; right: 0; height: 70px; z-index: 9999;
          display: flex; align-items: center; justify-content: space-between;
          padding: 0 4vw; background: rgba(255,255,255,.96); backdrop-filter: blur(8px);
          border-bottom: 1px solid #e6e9f4; box-shadow: 0 4px 18px rgba(27,37,89,.07); }
.brand { display: flex; align-items: center; gap: 10px; text-decoration: none !important;
         font-size: 1.45rem; font-weight: 800; color: #1b2559 !important; }
.brand img { height: 38px; }
.brand span b { background: linear-gradient(90deg,#4f46e5,#06b6d4); -webkit-background-clip: text;
                -webkit-text-fill-color: transparent; }
.navlinks { display: flex; gap: 6px; align-items: center; }
.navlinks a { text-decoration: none !important; color: #4a5380 !important; font-weight: 600;
              padding: 9px 16px; border-radius: 999px; font-size: .95rem; transition: all .2s; }
.navlinks a:hover { background: #eef0fb; color: #4f46e5 !important; }
.navlinks a.active { background: linear-gradient(90deg,#4f46e5,#7c3aed); color: #fff !important; }
.navcta { text-decoration: none !important; color: #fff !important; font-weight: 700; padding: 11px 22px;
          border-radius: 999px; background: linear-gradient(90deg,#f59e0b,#ef4444); font-size: .95rem;
          box-shadow: 0 6px 16px rgba(239,68,68,.3); }

/* ----- hero ----- */
.hero { display: flex; align-items: center; justify-content: space-between; gap: 30px; flex-wrap: wrap;
        padding: 56px 56px; border-radius: 28px; color: #fff;
        background: linear-gradient(120deg, #0b132b 0%, #2a2a8f 55%, #6d28d9 100%);
        box-shadow: 0 22px 50px rgba(43,42,143,.35); }
.hero .txt { flex: 1 1 380px; }
.hero .badge { display: inline-block; padding: 7px 16px; border-radius: 999px; font-size: .85rem; font-weight: 700;
               background: rgba(255,255,255,.15); color: #fff !important; margin-bottom: 18px; }
.hero h1 { color: #fff !important; font-size: 3.1rem; line-height: 1.12; margin: 0 0 16px; }
.hero h1 span { background: linear-gradient(90deg,#fbbf24,#fb7185); -webkit-background-clip: text;
                -webkit-text-fill-color: transparent; }
.stApp .hero p { color: #d6dcff !important; font-size: 1.15rem; line-height: 1.6; margin-bottom: 26px; }
.hero .pic { flex: 1 1 330px; text-align: center; }
.hero .pic img { max-width: 100%; max-height: 400px; border-radius: 20px; }
.btn { display: inline-block; text-decoration: none !important; font-weight: 700; padding: 14px 28px;
       border-radius: 14px; margin: 0 12px 10px 0; transition: transform .2s; }
.btn:hover { transform: translateY(-3px); }
.btn.primary { background: linear-gradient(90deg,#f59e0b,#ef4444); color: #fff !important;
               box-shadow: 0 10px 24px rgba(239,68,68,.4); }
.btn.ghost { background: rgba(255,255,255,.14); color: #fff !important; border: 1px solid rgba(255,255,255,.35); }

/* ----- stats strip ----- */
.stats { display: flex; flex-wrap: wrap; gap: 16px; margin: -34px 28px 10px; position: relative; z-index: 2; }
.stat { flex: 1 1 200px; background: #fff; border-radius: 20px; padding: 22px; text-align: center;
        box-shadow: 0 12px 30px rgba(27,37,89,.12); }
.stat h2 { margin: 0; font-size: 2.1rem; background: linear-gradient(90deg,#4f46e5,#06b6d4);
           -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.stApp .stat p { margin: 4px 0 0; color: #6b7399 !important; font-weight: 600; font-size: .92rem; }

/* ----- sections ----- */
.section-title { text-align: center; margin: 72px 0 8px; font-size: 2.2rem; }
.stApp .section-sub { text-align: center; color: #6b7399 !important; max-width: 640px; margin: 0 auto 28px; font-size: 1.05rem; }
.cards { display: flex; flex-wrap: wrap; gap: 20px; }
.fcard { flex: 1 1 250px; background: #fff; border-radius: 22px; padding: 28px; border: 1px solid #e9ecf7;
         box-shadow: 0 8px 24px rgba(27,37,89,.06); transition: all .25s; }
.fcard:hover { transform: translateY(-8px); box-shadow: 0 18px 38px rgba(79,70,229,.2); }
.fcard img { width: 64px; margin-bottom: 14px; }
.fcard h3 { margin: 0 0 8px; font-size: 1.25rem; }
.stApp .fcard p { color: #6b7399 !important; margin: 0 0 12px; line-height: 1.55; }
.fcard a { text-decoration: none !important; color: #4f46e5 !important; font-weight: 700; }
.steps { display: flex; flex-wrap: wrap; gap: 20px; }
.step { flex: 1 1 200px; text-align: center; padding: 10px; }
.step img { width: 74px; }
.step .num { display: inline-block; width: 30px; height: 30px; line-height: 30px; border-radius: 50%;
             background: #1b2559; color: #fff; font-weight: 700; margin: 10px 0 6px; }
.step h4 { margin: 4px 0; }
.stApp .step p { color: #6b7399 !important; font-size: .95rem; }
.why { display: flex; align-items: center; gap: 40px; flex-wrap: wrap; background: #fff; border-radius: 28px;
       padding: 40px; box-shadow: 0 10px 30px rgba(27,37,89,.08); margin-top: 50px; }
.why .pic { flex: 1 1 360px; } .why .pic img { width: 100%; border-radius: 18px; }
.why .txt { flex: 1 1 340px; }
.why li { margin-bottom: 12px; line-height: 1.55; list-style: none; padding-left: 0; }
.why li:before { content: "✔"; color: #10b981; font-weight: 800; margin-right: 10px; }
.why ul { padding-left: 0; }
.cta { margin-top: 50px; padding: 46px; border-radius: 28px; text-align: center; color: #fff;
       background: linear-gradient(120deg,#4f46e5,#7c3aed 55%,#ec4899); }
.cta h2 { color: #fff !important; margin: 0 0 8px; } .stApp .cta p { color: #f1ecff !important; margin-bottom: 22px; }
.footer { width: 100vw; position: relative; left: 50%; margin: 60px 0 0 -50vw; padding: 44px 8vw 22px; box-sizing: border-box; background: #0b132b; color: #aeb7e6; }
.footer .cols { display: flex; flex-wrap: wrap; gap: 40px; justify-content: space-between; }
.footer .col { flex: 1 1 220px; }
.footer h4 { color: #fff !important; margin-bottom: 12px; }
.stApp .footer p, .stApp .footer a { color: #aeb7e6 !important; text-decoration: none !important; display: block; margin: 6px 0; }
.footer a:hover { color: #fff !important; }
.footer .copy { border-top: 1px solid #25305c; margin-top: 28px; padding-top: 16px; text-align: center; font-size: .9rem; }

/* ----- inner page header, cards, kpis ----- */
.pagehead { padding: 34px 40px; border-radius: 24px; margin-bottom: 22px; color: #fff;
            background: linear-gradient(120deg,#4f46e5,#7c3aed 60%,#ec4899); box-shadow: 0 14px 34px rgba(79,70,229,.3); }
.pagehead h1 { color: #fff !important; margin: 0; font-size: 2.2rem; }
.stApp .pagehead p { color: #ece8ff !important; margin: 6px 0 0; font-size: 1.05rem; }
.kpi { padding: 20px; border-radius: 18px; text-align: center; color: #fff; box-shadow: 0 8px 20px rgba(27,37,89,.18);
       transition: transform .2s; }
.kpi:hover { transform: translateY(-5px); }
.kpi h2 { margin: 0; font-size: 2rem; color: #fff !important; } .stApp .kpi p { margin: 4px 0 0; color: #fff !important; opacity: .92; }
.c1 { background: linear-gradient(135deg,#06b6d4,#4f46e5); } .c2 { background: linear-gradient(135deg,#f59e0b,#fbbf24); }
.c3 { background: linear-gradient(135deg,#ef4444,#fb7185); } .c4 { background: linear-gradient(135deg,#10b981,#06b6d4); }
.c5 { background: linear-gradient(135deg,#7c3aed,#ec4899); }
.stApp .c2 h2, .stApp .c2 p { color: #3a2a00 !important; }
.card { padding: 20px; border-radius: 18px; background: #fff; border: 1px solid #e9ecf7;
        box-shadow: 0 6px 18px rgba(27,37,89,.06); margin-bottom: 14px; }
.good { padding: 18px; border-radius: 16px; background: linear-gradient(135deg,#10b981,#34d399);
        color: #053b2b !important; font-size: 1.3rem; font-weight: 800; text-align: center; }
.bad  { padding: 18px; border-radius: 16px; background: linear-gradient(135deg,#ef4444,#fb7185);
        color: #fff !important; font-size: 1.3rem; font-weight: 800; text-align: center; }
.stButton > button { background: linear-gradient(90deg,#f59e0b,#ef4444); color: #fff; border: none;
        border-radius: 12px; padding: 10px 28px; font-weight: 700; }
.stApp .stButton > button p { color: #fff !important; font-weight: 700; }
.stButton > button:hover { color: #fff; filter: brightness(1.08); }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

PLOT = dict(template="plotly_white", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#1b2559"))
STATUS_COLORS = {"Genuine": "#10b981", "Fraud": "#ef4444"}


# ---------- 2. SMALL HELPERS ----------
def html(text):
    """Show HTML. We remove indentation and blank lines so Markdown does not break it."""
    clean = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    st.markdown(clean, unsafe_allow_html=True)


def svg_img(svg, cls=""):
    data = base64.b64encode(svg.encode()).decode()
    return f'<img class="{cls}" src="data:image/svg+xml;base64,{data}">'


def picture(photo_file, svg):
    """Use YOUR photo from the images/ folder if it exists, otherwise our drawn illustration."""
    path = ROOT / "images" / photo_file
    if path.exists():
        ext = photo_file.split(".")[-1].lower().replace("jpg", "jpeg")
        data = base64.b64encode(path.read_bytes()).decode()
        return f'<img src="data:image/{ext};base64,{data}">'
    return svg_img(svg)          # svg = raw SVG text


def kpi(col, css, value, label):
    col.markdown(f'<div class="kpi {css}"><h2>{value}</h2><p>{label}</p></div>', unsafe_allow_html=True)


def page_head(title, sub):
    html(f'<div class="pagehead"><h1>{title}</h1><p>{sub}</p></div>')


# ---------- 3. DATA + MODEL (same steps as the notebook) ----------
DROP_COLS = ["fraud_reported", "is_fraud", "policy_number", "insured_zip", "incident_location",
             "auto_model", "policy_bind_date", "incident_date", "auto_year"]


def prepare(raw):
    d = raw.copy()
    if "auto_model" in d.columns:
        d["auto_model"] = d["auto_model"].astype(str)
    if "authorities_contacted" in d.columns:
        d["authorities_contacted"] = d["authorities_contacted"].fillna("None")
    else:
        d["authorities_contacted"] = "None"
    d = d.replace("?", "Unknown")
    if "incident_date" in d.columns and "policy_bind_date" in d.columns:
        incident_dates = pd.to_datetime(d["incident_date"], format="%d-%m-%Y", errors="coerce")
        policy_dates = pd.to_datetime(d["policy_bind_date"], format="%d-%m-%Y", errors="coerce")
        d["policy_age_days"] = (incident_dates - policy_dates).dt.days
    elif "policy_age_days" not in d.columns:
        d["policy_age_days"] = np.nan
    if "auto_year" in d.columns:
        d["vehicle_age"] = 2015 - pd.to_numeric(d["auto_year"], errors="coerce")
    elif "vehicle_age" not in d.columns:
        d["vehicle_age"] = np.nan
    return d


@st.cache_data
def load_data():
    d = prepare(pd.read_csv(FILE))
    d["is_fraud"] = (d["fraud_reported"] == "Y").astype(int)
    d["Status"] = d["is_fraud"].map({0: "Genuine", 1: "Fraud"})
    return d


df = load_data()
X_all = df.drop(columns=[c for c in DROP_COLS + ["Status"] if c in df.columns])
y_all = df["is_fraud"]
FEATURES = X_all.columns.tolist()
CAT_COLS = [c for c in X_all.columns if not pd.api.types.is_numeric_dtype(X_all[c])]
NUM_COLS = [c for c in FEATURES if c not in CAT_COLS]
DEFAULTS = {c: (X_all[c].mode()[0] if c in CAT_COLS else X_all[c].median()) for c in FEATURES}


def make_preprocess():
    return ColumnTransformer([("numbers", StandardScaler(), NUM_COLS),
                              ("text", OneHotEncoder(handle_unknown="ignore"), CAT_COLS)])


def make_final_classifier(weight):
    if XGBClassifier is None:
        return GradientBoostingClassifier(n_estimators=100, max_depth=4, learning_rate=0.03,
                                          random_state=42)
    return XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.03,
                         scale_pos_weight=weight, random_state=42, eval_metric="logloss")


@st.cache_resource
def train_model():
    X_tr, X_te, y_tr, y_te = train_test_split(X_all, y_all, test_size=0.2, random_state=42, stratify=y_all)
    weight = (y_tr == 0).sum() / (y_tr == 1).sum()
    model = Pipeline([("prep", make_preprocess()),
                      ("model", make_final_classifier(weight))])
    cv = StratifiedKFold(5, shuffle=True, random_state=42)
    oof = cross_val_predict(model, X_tr, y_tr, cv=cv, method="predict_proba")[:, 1]
    p, r, t = precision_recall_curve(y_tr, oof)
    threshold = t[np.argmax((2 * p * r / (p + r + 1e-9))[:-1])]
    model.fit(X_tr, y_tr)
    return model, threshold, X_tr, X_te, y_tr, y_te


model, THRESHOLD, X_train, X_test, y_train, y_test = train_model()
test_proba = model.predict_proba(X_test)[:, 1]
test_pred = (test_proba >= THRESHOLD).astype(int)


@st.cache_data
def compare_models():
    weight = (y_train == 0).sum() / (y_train == 1).sum()
    models = {
        "Logistic Regression": LogisticRegression(class_weight="balanced", max_iter=1000),
        "KNN": KNeighborsClassifier(),
        "SVM": SVC(class_weight="balanced", probability=True, random_state=42),
        "Decision Tree": DecisionTreeClassifier(max_depth=5, class_weight="balanced", random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=300, class_weight="balanced_subsample",
                                                random_state=42, n_jobs=-1),
        "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    }
    if XGBClassifier is not None:
        models["XGBoost"] = XGBClassifier(n_estimators=200, max_depth=3, learning_rate=0.05,
                                          scale_pos_weight=weight, random_state=42, eval_metric="logloss")
    cv = StratifiedKFold(5, shuffle=True, random_state=42)
    rows = []
    for name, m in models.items():
        s = cross_validate(Pipeline([("prep", make_preprocess()), ("model", m)]), X_train, y_train, cv=cv,
                           scoring=["accuracy", "precision", "recall", "f1", "roc_auc"])
        rows.append({"Model": name, "Accuracy": s["test_accuracy"].mean(), "Precision": s["test_precision"].mean(),
                     "Recall": s["test_recall"].mean(), "F1": s["test_f1"].mean(), "ROC-AUC": s["test_roc_auc"].mean()})
    return pd.DataFrame(rows).set_index("Model").round(3).sort_values("F1", ascending=False)


def show_verdict(prob):
    if prob >= THRESHOLD:
        st.markdown('<div class="bad">🚨 SUSPICIOUS - send to investigator</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="good">✅ Looks genuine</div>', unsafe_allow_html=True)


# ---------- 4. NAVIGATION BAR (real links, like a website) ----------
PAGES = {"home": "Home", "dashboard": "Dashboard", "check": "Check a Claim",
         "batch": "Batch Check", "models": "Models", "about": "About"}
page = st.query_params.get("page", "home")
if page not in PAGES:
    page = "home"

links = "".join(f'<a href="?page={k}" target="_self" class="{"active" if k == page else ""}">{v}</a>'
                for k, v in PAGES.items())
html(f'''<div class="navbar">
<a class="brand" href="?page=home" target="_self">{svg_img(art.LOGO)}<span>{BRAND}<b>AI</b></span></a>
<div class="navlinks">{links}</div>
<a class="navcta" href="?page=check" target="_self">Check a claim</a>
</div>''')


# ---------- 5. FOOTER ----------
def footer():
    html(f'''<div class="footer"><div class="cols">
    <div class="col"><h4>{BRAND}<b>AI</b></h4>
    <p>AI that scores every insurance claim for fraud risk, so investigators can focus on the claims that matter.</p></div>
    <div class="col"><h4>Explore</h4>
    <a href="?page=dashboard" target="_self">Fraud Dashboard</a><a href="?page=check" target="_self">Check a Claim</a>
    <a href="?page=batch" target="_self">Batch Check</a><a href="?page=models" target="_self">Model Comparison</a></div>
    <div class="col"><h4>Contact</h4><p>✉ contact@yourcompany.com</p><p>☎ +00 00000 00000</p><p>📍 Your City, Your Country</p></div>
    </div><div class="copy">© 2026 {BRAND}AI. All rights reserved. Demo project built with Python and Streamlit.</div></div>''')


# =====================================================
#  HOME  (company landing page)
# =====================================================
if page == "home":
    recall = recall_score(y_test, test_pred) * 100
    html(f'''<div class="hero"><div class="txt">
    <span class="badge">🛡️ AI-powered insurance fraud detection</span>
    <h1>Catch suspicious claims <span>before they cost you money</span></h1>
    <p>{BRAND}AI gives every insurance claim a fraud score in seconds, so your investigators can
    check the riskiest claims first.</p>
    <a class="btn primary" href="?page=check" target="_self">Check a claim</a>
    <a class="btn ghost" href="?page=dashboard" target="_self">View dashboard</a></div>
    <div class="pic">{picture("hero.jpg", art.HERO)}</div></div>
    <div class="stats">
    <div class="stat"><h2>{len(df):,}</h2><p>Claims analysed</p></div>
    <div class="stat"><h2>{df.is_fraud.mean() * 100:.0f}%</h2><p>Claims were fraud</p></div>
    <div class="stat"><h2>{recall:.0f}%</h2><p>Frauds caught (test data)</p></div>
    <div class="stat"><h2>{MODEL_COMPARISON_COUNT}</h2><p>Models compared</p></div></div>''')

    html('<h2 class="section-title">Our Solutions</h2>'
         '<div class="section-sub">Everything your claims team needs to find fraud faster, in one place.</div>')
    html(f'''<div class="cards">
    <div class="fcard">{svg_img(art.ICONS["dashboard"])}<h3>Fraud Dashboard</h3>
    <p>See where fraud happens: by incident type, severity, hobby and claim amount.</p>
    <a href="?page=dashboard" target="_self">Open dashboard →</a></div>
    <div class="fcard">{svg_img(art.ICONS["search"])}<h3>Instant Claim Check</h3>
    <p>Enter the details of one claim and get a fraud score with a clear verdict.</p>
    <a href="?page=check" target="_self">Check a claim →</a></div>
    <div class="fcard">{svg_img(art.ICONS["upload"])}<h3>Batch Scoring</h3>
    <p>Upload hundreds of claims and download a report ranked from most to least risky.</p>
    <a href="?page=batch" target="_self">Upload claims →</a></div>
    <div class="fcard">{svg_img(art.ICONS["models"])}<h3>Model Transparency</h3>
    <p>Compare {MODEL_COMPARISON_COUNT} machine learning models and see how the final model performs.</p>
    <a href="?page=models" target="_self">See results →</a></div></div>''')

    html('<h2 class="section-title">How It Works</h2>'
         '<div class="section-sub">From raw claim data to a clear fraud alert in four simple steps.</div>')
    html(f'''<div class="steps">
    <div class="step">{svg_img(art.ICONS["data"])}<br><span class="num">1</span><h4>Collect claims</h4>
    <p>Customer, policy, accident and claim amount details.</p></div>
    <div class="step">{svg_img(art.ICONS["features"])}<br><span class="num">2</span><h4>Prepare features</h4>
    <p>Clean the data and add useful features like policy age.</p></div>
    <div class="step">{svg_img(art.ICONS["models"])}<br><span class="num">3</span><h4>Score with AI</h4>
    <p>{FINAL_MODEL_NAME} gives each claim a fraud score.</p></div>
    <div class="step">{svg_img(art.ICONS["alert"])}<br><span class="num">4</span><h4>Alert investigators</h4>
    <p>Claims above the cutoff are flagged for a human check.</p></div></div>''')

    html(f'''<div class="why"><div class="pic">{picture("dashboard.jpg", art.DASH_MOCK)}</div>
    <div class="txt"><h2>Why teams choose {BRAND}AI</h2>
    <ul><li><b>Finds most frauds:</b> it caught {recall:.0f}% of the fraud claims in our hidden test data.</li>
    <li><b>Clear and simple:</b> one fraud score per claim, with a green or red verdict.</li>
    <li><b>Built for imbalanced data:</b> only about {df.is_fraud.mean() * 100:.0f}% of claims are fraud, so we judge
    models by recall and F1, not just accuracy.</li>
    <li><b>Human in control:</b> the score is a guide, and every flagged claim is checked by a person.</li></ul></div></div>
    <div class="cta"><h2>Ready to find risky claims faster?</h2>
    <p>Try the live demo with a single claim, or upload a whole file.</p>
    <a class="btn primary" href="?page=check" target="_self">Check a claim</a>
    <a class="btn ghost" href="?page=batch" target="_self">Batch check</a></div>''')
    footer()

# =====================================================
#  DASHBOARD
# =====================================================
elif page == "dashboard":
    page_head("Fraud Dashboard", "Explore fraud patterns across 1,000 insurance claims.")

    with st.expander("🎛️ Filters", expanded=True):
        a, b, c = st.columns(3)
        sev = a.multiselect("Incident severity", sorted(df.incident_severity.unique()),
                            default=sorted(df.incident_severity.unique()))
        inc = b.multiselect("Incident type", sorted(df.incident_type.unique()),
                            default=sorted(df.incident_type.unique()))
        lo, hi = int(df.total_claim_amount.min()), int(df.total_claim_amount.max())
        amt = c.slider("Total claim amount", lo, hi, (lo, hi))
    f = df[df.incident_severity.isin(sev) & df.incident_type.isin(inc) & df.total_claim_amount.between(*amt)]

    if f.empty:
        st.warning("No claims match these filters. Please change the filters.")
    else:
        c1, c2, c3, c4 = st.columns(4)
        kpi(c1, "c1", f"{len(f):,}", "Claims (filtered)")
        kpi(c2, "c3", f"{f['is_fraud'].sum():,}", "Fraud Claims")
        kpi(c3, "c2", f"{f['is_fraud'].mean() * 100:.1f}%", "Fraud Rate")
        kpi(c4, "c5", f"{f.loc[f.is_fraud == 1, 'total_claim_amount'].sum():,.0f}", "Claim Value in Fraud Cases")
        st.write("")

        col1, col2 = st.columns(2)
        with col1:
            r = f.groupby("incident_severity")["is_fraud"].mean().mul(100).reset_index()
            fig = px.bar(r, x="incident_severity", y="is_fraud", color="incident_severity", text_auto=".1f",
                         title="Fraud Rate (%) by Incident Severity",
                         color_discrete_sequence=px.colors.qualitative.Bold)
            fig.update_layout(**PLOT, showlegend=False, xaxis_title="", yaxis_title="Fraud rate (%)")
            st.plotly_chart(fig, width="stretch")
        with col2:
            cnt = f["Status"].value_counts().reset_index()
            cnt.columns = ["Status", "Count"]
            fig = px.pie(cnt, names="Status", values="Count", hole=0.55, color="Status",
                         color_discrete_map=STATUS_COLORS, title="Fraud vs Genuine Claims")
            fig.update_layout(**PLOT)
            st.plotly_chart(fig, width="stretch")

        col3, col4 = st.columns(2)
        with col3:
            r = f.groupby("insured_hobbies")["is_fraud"].mean().mul(100).sort_values().reset_index()
            fig = px.bar(r, x="is_fraud", y="insured_hobbies", orientation="h", color="is_fraud",
                         color_continuous_scale="Sunsetdark", title="Fraud Rate (%) by Insured Hobby")
            fig.update_layout(**PLOT, coloraxis_showscale=False, xaxis_title="Fraud rate (%)", yaxis_title="")
            st.plotly_chart(fig, width="stretch")
        with col4:
            fig = px.box(f, x="Status", y="total_claim_amount", color="Status", color_discrete_map=STATUS_COLORS,
                         title="Total Claim Amount: Fraud vs Genuine")
            fig.update_layout(**PLOT, showlegend=False, xaxis_title="")
            st.plotly_chart(fig, width="stretch")

        col5, col6 = st.columns(2)
        with col5:
            r = f.groupby("incident_type")["is_fraud"].mean().mul(100).reset_index()
            fig = px.bar(r, x="incident_type", y="is_fraud", color="incident_type", text_auto=".1f",
                         title="Fraud Rate (%) by Incident Type", color_discrete_sequence=px.colors.qualitative.Vivid)
            fig.update_layout(**PLOT, showlegend=False, xaxis_title="", yaxis_title="Fraud rate (%)")
            st.plotly_chart(fig, width="stretch")
        with col6:
            fig = px.histogram(f, x="age", color="Status", nbins=30, barmode="overlay", opacity=0.75,
                               color_discrete_map=STATUS_COLORS, title="Customer Age Distribution")
            fig.update_layout(**PLOT)
            st.plotly_chart(fig, width="stretch")

        corr = f[["months_as_customer", "age", "policy_annual_premium", "total_claim_amount", "injury_claim",
                  "property_claim", "vehicle_claim", "policy_age_days", "is_fraud"]].corr().round(2)
        fig = px.imshow(corr, text_auto=True, color_continuous_scale="Turbo", title="Correlation Heatmap")
        fig.update_layout(**PLOT, height=520)
        st.plotly_chart(fig, width="stretch")

        with st.expander("📄 View / download filtered data"):
            shown = f.drop(columns=["is_fraud", "Status"])
            st.dataframe(shown, width="stretch")
            st.download_button("⬇️ Download CSV", shown.to_csv(index=False).encode(), "filtered_claims.csv", "text/csv")
    footer()

# =====================================================
#  CHECK ONE CLAIM
# =====================================================
elif page == "check":
    page_head("Check a Claim", "Fill in the claim details and get a fraud score. Fields not shown use typical values.")

    opts = lambda col: sorted(df[col].unique().tolist())
    tab1, tab2, tab3 = st.tabs(["🚗 Incident", "💰 Claim Amounts", "👤 Customer & Policy"])
    with tab1:
        a, b = st.columns(2)
        severity = a.selectbox("Incident severity", opts("incident_severity"),
                               index=opts("incident_severity").index("Major Damage"))
        incident_type = b.selectbox("Incident type", opts("incident_type"))
        collision = a.selectbox("Collision type", opts("collision_type"))
        authorities = b.selectbox("Authorities contacted", opts("authorities_contacted"))
        prop_damage = a.selectbox("Property damage", opts("property_damage"))
        police = b.selectbox("Police report available", opts("police_report_available"))
        vehicles = a.slider("Vehicles involved", 1, 4, 1)
        injuries = b.slider("Bodily injuries", 0, 2, 0)
        witnesses = a.slider("Witnesses", 0, 3, 1)
        hour = b.slider("Hour of the day", 0, 23, 12)
    with tab2:
        a, b, c = st.columns(3)
        injury_claim = a.number_input("Injury claim", 0, 100000, 7000, step=500)
        property_claim = b.number_input("Property claim", 0, 100000, 7000, step=500)
        vehicle_claim = c.number_input("Vehicle claim", 0, 200000, 40000, step=1000)
        st.info(f"Total claim amount: **{injury_claim + property_claim + vehicle_claim:,}**")
    with tab3:
        a, b = st.columns(2)
        hobby = a.selectbox("Insured hobby", opts("insured_hobbies"))
        age = b.slider("Customer age", 19, 70, 40)
        months = a.slider("Months as customer", 0, 480, 200)
        policy_age = b.slider("Days from policy start to accident", 0, 9000, 4000)
        veh_age = a.slider("Vehicle age (years)", 0, 25, 10)
        csl = b.selectbox("Policy CSL", opts("policy_csl"))
        deductable = a.selectbox("Policy deductible", [500, 1000, 2000], index=1)
        premium = b.slider("Annual premium", 400.0, 2200.0, 1250.0, 10.0)
        umbrella = a.number_input("Umbrella limit", 0, 10000000, 0, step=1000000)

    if st.button("🚀 Check Fraud Risk"):
        row = dict(DEFAULTS)
        row.update({"incident_severity": severity, "incident_type": incident_type, "collision_type": collision,
                    "authorities_contacted": authorities, "property_damage": prop_damage,
                    "police_report_available": police, "number_of_vehicles_involved": vehicles,
                    "bodily_injuries": injuries, "witnesses": witnesses, "incident_hour_of_the_day": hour,
                    "injury_claim": injury_claim, "property_claim": property_claim, "vehicle_claim": vehicle_claim,
                    "total_claim_amount": injury_claim + property_claim + vehicle_claim,
                    "insured_hobbies": hobby, "age": age, "months_as_customer": months,
                    "policy_age_days": policy_age, "vehicle_age": veh_age, "policy_csl": csl,
                    "policy_deductable": deductable, "policy_annual_premium": premium, "umbrella_limit": umbrella})
        prob = model.predict_proba(pd.DataFrame([row])[FEATURES])[0, 1]

        left, right = st.columns(2)
        with left:
            show_verdict(prob)
            gauge = go.Figure(go.Indicator(
                mode="gauge+number", value=prob * 100, number={"suffix": "%"}, title={"text": "Fraud Score"},
                gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#1b2559"},
                       "steps": [{"range": [0, THRESHOLD * 100], "color": "#34d399"},
                                 {"range": [THRESHOLD * 100, 60], "color": "#fbbf24"},
                                 {"range": [60, 100], "color": "#fb7185"}],
                       "threshold": {"line": {"color": "#1b2559", "width": 4}, "value": THRESHOLD * 100}}))
            gauge.update_layout(**PLOT, height=330)
            st.plotly_chart(gauge, width="stretch")
            st.caption(f"Claims with a score above {THRESHOLD * 100:.0f}% (dark line) are flagged.")
        with right:
            st.markdown("#### 🔎 What the past data says")
            sev_rate = df.loc[df.incident_severity == severity, "is_fraud"].mean() * 100
            hob_rate = df.loc[df.insured_hobbies == hobby, "is_fraud"].mean() * 100
            st.markdown(f'<div class="card">In this dataset, <b>{sev_rate:.0f}%</b> of claims with severity '
                        f'<b>{severity}</b> were fraud.<br><br>'
                        f'<b>{hob_rate:.0f}%</b> of claims where the hobby is <b>{hobby}</b> were fraud.<br><br>'
                        f'Overall fraud rate is <b>{df.is_fraud.mean() * 100:.0f}%</b>.</div>', unsafe_allow_html=True)
            st.info("The score is a guide, not proof. A flagged claim should be checked by a person.")
    footer()

# =====================================================
#  BATCH CHECK
# =====================================================
elif page == "batch":
    page_head("Batch Check", "Upload many claims and get a report ranked from most to least risky.")
    st.caption("Use an Excel or CSV file with the same columns as the training data.")

    up = st.file_uploader("Upload claims file", type=["xlsx", "csv"])
    use_sample = st.checkbox("No file? Try with 50 sample claims from the dataset")

    raw = None
    if up is not None:
        raw = pd.read_excel(up) if up.name.endswith("xlsx") else pd.read_csv(up)
    elif use_sample:
        raw = pd.read_csv(FILE).sample(50, random_state=1)

    if raw is not None and "auto_model" in raw.columns:
        raw["auto_model"] = raw["auto_model"].astype(str)

    if raw is not None:
        try:
            prepared = prepare(raw)
            missing = [column for column in FEATURES if column not in prepared.columns]
            if missing:
                st.error("Your file is missing required columns: " + ", ".join(missing))
                footer()
                st.stop()
            scores = model.predict_proba(prepared[FEATURES])[:, 1]
        except (KeyError, TypeError, ValueError) as e:
            st.error(f"Could not score this file: {e}")
            footer()
            st.stop()

        out = raw.copy()
        out["fraud_score_%"] = (scores * 100).round(1)
        out["flag"] = np.where(scores >= THRESHOLD, "SUSPICIOUS", "Looks genuine")
        out = out.sort_values("fraud_score_%", ascending=False)

        c1, c2, c3 = st.columns(3)
        kpi(c1, "c1", f"{len(out):,}", "Claims Scored")
        kpi(c2, "c3", f"{(out['flag'] == 'SUSPICIOUS').sum():,}", "Flagged Suspicious")
        kpi(c3, "c4", f"{out['fraud_score_%'].mean():.1f}%", "Average Fraud Score")
        st.write("")
        fig = px.histogram(out, x="fraud_score_%", nbins=25, color="flag", title="Fraud score distribution",
                           color_discrete_map={"SUSPICIOUS": "#ef4444", "Looks genuine": "#10b981"})
        fig.update_layout(**PLOT)
        st.plotly_chart(fig, width="stretch")
        st.dataframe(out, width="stretch")
        st.download_button("⬇️ Download ranked report", out.to_csv(index=False).encode(), "fraud_report.csv", "text/csv")
    else:
        st.info("👆 Upload a file or tick the sample box to start.")
    footer()

# =====================================================
#  MODEL COMPARISON
# =====================================================
elif page == "models":
    page_head("Model Comparison", f"How {MODEL_COMPARISON_COUNT} machine learning models perform, and how the final model does on test data.")
    tab1, tab2 = st.tabs([f"📈 Compare {MODEL_COMPARISON_COUNT} Models", "🏆 Final Model (Test Data)"])

    with tab1:
        st.caption("5-fold cross-validation on the training data. The first run takes a few seconds.")
        with st.spinner(f"Training {MODEL_COMPARISON_COUNT} models..."):
            res = compare_models()
        st.dataframe(res, width="stretch")
        fig = px.bar(res.reset_index().melt(id_vars="Model", value_vars=["Recall", "F1", "ROC-AUC"]),
                     x="Model", y="value", color="variable", barmode="group", title="Recall, F1 and ROC-AUC",
                     color_discrete_sequence=["#06b6d4", "#f59e0b", "#ef4444"])
        fig.update_layout(**PLOT, yaxis_range=[0, 1], legend_title="Metric", yaxis_title="")
        st.plotly_chart(fig, width="stretch")
        st.info("Scores of the top models are close because the data is small (1,000 claims). "
                "Random Forest has a good ROC-AUC but low recall at the default 0.5 cutoff.")

    with tab2:
        c1, c2, c3, c4, c5 = st.columns(5)
        kpi(c1, "c1", f"{accuracy_score(y_test, test_pred):.3f}", "Accuracy")
        kpi(c2, "c4", f"{precision_score(y_test, test_pred):.3f}", "Precision")
        kpi(c3, "c2", f"{recall_score(y_test, test_pred):.3f}", "Recall")
        kpi(c4, "c3", f"{f1_score(y_test, test_pred):.3f}", "F1 Score")
        kpi(c5, "c5", f"{roc_auc_score(y_test, test_proba):.3f}", "ROC-AUC")
        st.write("")
        col1, col2 = st.columns(2)
        with col1:
            fig = px.imshow(confusion_matrix(y_test, test_pred), text_auto=True, color_continuous_scale="Purples",
                            x=["Genuine", "Fraud"], y=["Genuine", "Fraud"],
                            labels=dict(x="Predicted", y="Actual"), title="Confusion Matrix")
            fig.update_layout(**PLOT)
            st.plotly_chart(fig, width="stretch")
        with col2:
            fpr, tpr, _ = roc_curve(y_test, test_proba)
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", name=FINAL_MODEL_NAME,
                                     line=dict(color="#4f46e5", width=4)))
            fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", name="Random guess",
                                     line=dict(color="gray", dash="dash")))
            fig.update_layout(**PLOT, title="ROC Curve", xaxis_title="False Positive Rate",
                              yaxis_title="True Positive Rate")
            st.plotly_chart(fig, width="stretch")

        names = [n.replace("numbers__", "").replace("text__", "")
                 for n in model.named_steps["prep"].get_feature_names_out()]
        imp = pd.Series(model.named_steps["model"].feature_importances_, index=names)
        imp = imp.sort_values().tail(12).reset_index()
        imp.columns = ["Feature", "Importance"]
        fig = px.bar(imp, x="Importance", y="Feature", orientation="h", color="Importance",
                     color_continuous_scale="Sunsetdark", title="Top 12 Features")
        fig.update_layout(**PLOT, coloraxis_showscale=False)
        st.plotly_chart(fig, width="stretch")
    footer()

# =====================================================
#  ABOUT
# =====================================================
else:
    page_head("About This Project", "The problem, the data and the method behind FraudShield AI.")
    html(f'''<div class="card"><h3>Problem</h3>
    Insurance fraud costs companies a lot of money, and checking every claim by hand is slow.
    This app gives each claim a fraud score so investigators can check the riskiest claims first.</div>
    <div class="card"><h3>Dataset</h3>
    1,000 auto insurance claims with customer, policy, accident and claim amount details.
    About 25% of the claims are fraud.</div>
    <div class="card"><h3>Method</h3>
    1. Kept the <b>?</b> values as an "Unknown" category and fixed the "None" value<br>
    2. Created new features: policy age in days and vehicle age<br>
    3. Removed ID-like columns<br>
    4. Compared {MODEL_COMPARISON_COUNT} models with 5-fold cross-validation<br>
    5. Used {FINAL_MODEL_NAME} and chose the alert cutoff using training data only</div>
    <div class="card"><h3>Tech Stack</h3>Python, Pandas, NumPy, Scikit-learn, {FINAL_MODEL_NAME}, Plotly, Streamlit</div>''')
    footer()