# app.py  -- Creative UI + Contact page (replace your current app.py with this)
import os
import pickle
import pandas as pd
import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")

# -------------------------
# CSS — animated background + glass card styling
# -------------------------
CUSTOM_CSS = """
/* full app animated gradient */
.stApp {
  background: linear-gradient(120deg, #071036 0%, #0f172a 30%, #0ea5a2 70%, #7c3aed 100%);
  background-size: 300% 300%;
  animation: gradientShift 18s ease infinite;
  color: #e6eef8;
  min-height: 100vh;
}

/* gradient animation */
@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* floating soft blobs */
.blob {
  position: absolute;
  width: 360px;
  height: 360px;
  border-radius: 50%;
  filter: blur(100px);
  opacity: 0.18;
  z-index: 0;
  pointer-events: none;
}
.blob.one { background: rgba(255,255,255,0.06); top: -100px; left: -80px; transform: rotate(10deg); }
.blob.two { background: rgba(255,255,255,0.04); bottom: -140px; right: -100px; transform: rotate(-10deg); }

/* glass card for content */
.main-card {
  position: relative;
  z-index: 1;
  padding: 26px;
  border-radius: 16px;
  background: rgba(255,255,255,0.03);
  box-shadow: 0 10px 30px rgba(2,6,23,0.6);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,0.05);
}

/* header */
.app-title {
  font-size: 22px;
  font-weight: 700;
  letter-spacing: 0.3px;
}
.app-sub {
  font-size: 12px;
  color: rgba(255,255,255,0.78);
}

/* button style */
.stButton>button {
  background: linear-gradient(90deg,#06b6d4,#10b981);
  color: white;
  border-radius: 10px;
  padding: 8px 14px;
  font-weight: 600;
  border: none;
  box-shadow: 0 6px 18px rgba(2,6,23,0.4);
}
.stButton>button:hover { transform: translateY(-1px); }

/* sidebar subtle */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  border-right: 1px solid rgba(255,255,255,0.03);
}
"""

st.markdown(f"<style>{CUSTOM_CSS}</style>", unsafe_allow_html=True)

# floating blobs
st.markdown(
    """
    <div class="blob one"></div>
    <div class="blob two"></div>
    """,
    unsafe_allow_html=True,
)


# -------------------------
# Load model (kept same as original)
# -------------------------
st.header("Heart Disease Prediction Using Machine Learning")

# description text (kept from original)
data = '''Project Objective
Heart Disease Prediction using Machine Learning
Heart disease prevention is critical, and data-driven prediction systems can significantly aid in early diagnosis and treatment. Machine Learning offers accurate prediction capabilities, enhancing healthcare outcomes.
In this project, I analyzed a heart disease dataset with appropriate preprocessing. Multiple classification algorithms were implemented in Python using Scikit-learn and Keras to predict the presence of heart disease.

Algorithms Used:
- Logistic Regression
- Naive Bayes
- Support Vector Machine (Linear)
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- XGBoost
- Artificial Neural Network (1 Hidden Layer, Keras)'''

# Path to the .pkl file inside ml_model
model_path = os.path.join(os.path.dirname(__file__), "model", "Heart_disease_pred.pkl")

with open(model_path, "rb") as f:
    chatgpt = pickle.load(f)

st.subheader(data)
st.image('https://t-shikuro.github.io/images/heart/heart.gif')


# -------------------------
# Sidebar navigation + Contact form (Google Form embed)
# -------------------------
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Contact Us"])

# Replace this with your real Google Form "share" link.
# To embed: open your Google Form -> Send -> Embed HTML -> copy src URL inside <iframe src="...">
# Example embed src: "https://docs.google.com/forms/d/e/<FORM_ID>/viewform?embedded=true"
FORM_EMBED_URL = "https://docs.google.com/forms/d/e/1FAIpQLSd_0nyMT5GeI2zG_ObYy07gSNKKeT-wH4TiQXKqAUXTINxrMg/viewform?embedded=true"

if page == "Contact Us":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.markdown("## Contact Us")
    st.markdown("We'd love to hear from you — feedback, bugs, or suggestions. Use the form below or open it in a new tab.")
    # Try to embed the Google Form. If embedding is blocked by browser, show open link fallback.
    iframe = f"""
        <iframe src="{FORM_EMBED_URL}" width="700" height="900" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    """
    st.markdown(iframe, unsafe_allow_html=True)
    # fallback link
    st.markdown("---")
    st.markdown(
    "If the form above doesn't load, open it here: "
    "[Open Contact Form](https://docs.google.com/forms/d/e/1FAIpQLSd_0nyMT5GeI2zG_ObYy07gSNKKeT-wH4TiQXKqAUXTINxrMg/viewform)"
)
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()  # don't run the rest of the app when on contact page


# -------------------------
# Main Home Page: Prediction UI (kept your logic, re-arranged inside card)
# -------------------------
# Load dataset (same as original)
csv_path = os.path.join(os.path.dirname(__file__), "heart.csv")
df = pd.read_csv(csv_path)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

# page header block (left)
st.markdown(
    """
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
      <div style="font-size:34px">❤️</div>
      <div>
        <div class="app-title">Heart Disease Predictor</div>
        <div class="app-sub">Fast predictions using pre-trained models — keep your doctor informed.</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Two-column layout: inputs | outputs
left_col, right_col = st.columns([1, 1.2], gap="large")

with left_col:
    st.subheader("Inputs")
    st.image("https://tse4.mm.bing.net/th/id/OIP.7LA1z7w-drtQmnFmC0KBNAHaE7?cb=thfvnext&pid=ImgDet&w=201&h=134&c=7&o=7&rm=3", width=200)
    all_values = []
    random.seed(11)
    for i in df.iloc[:, :-1]:
        min_value, max_value = df[i].agg(['min', 'max'])
        var = st.slider(f'Select {i} value', int(min_value), int(max_value),
                        random.randint(int(min_value), int(max_value)))
        all_values.append(var)

    final_value = [all_values]
    run = st.button("Run Model")

with right_col:
    st.subheader("Result")
    result_placeholder = st.empty()
    anim_placeholder = st.empty()

    # show animated heart while predicting (same gif but smaller)
    if run:
        progress_bar = st.progress(0)
        anim_placeholder.image('https://media1.tenor.com/m/LLlSFiqwJGMAAAAC/beating-heart-gif.gif', width=200)
        for i in range(100):
            time.sleep(0.02)
            progress_bar.progress(i + 1)

        # make prediction
        ans = chatgpt.predict(final_value)[0]

        anim_placeholder.empty()
        progress_bar.empty()

        if ans == 0:
            result_placeholder.success("No Heart Disease Detected ✅\n\nNote: This is a prediction — consult a doctor for diagnosis.")
        else:
            result_placeholder.warning("Heart Disease Found ⚠️\n\nThis prediction suggests possible heart disease — seek medical advice.")
    else:
        st.info("Set the input sliders and press **Run Model** to predict.")

# small footer / credits
st.markdown("---")
st.markdown("Made with ❤️ — Replace the contact form ID in `FORM_EMBED_URL` with your Google Form's embed URL.")
st.markdown('</div>', unsafe_allow_html=True)
