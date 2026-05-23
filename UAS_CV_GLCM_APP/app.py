import streamlit as st
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

from train_model import train_model
from glcm_feature import extract_glcm_features

# =====================
# KONFIGURASI
# =====================
st.set_page_config(
    page_title="GLCM Object Recognition",
    page_icon="🧠",
    layout="centered"
)

# =====================
# HEADER
# =====================
st.markdown("""
<h1 style='text-align:center;'>🧠 Aplikasi Pengenalan Objek</h1>
<h3 style='text-align:center;'>Metode GLCM & Decision Tree</h3>
<hr>
""", unsafe_allow_html=True)

# =====================
# LOAD MODEL
# =====================
@st.cache_resource
def load_model():
    return train_model()

model, accuracy, total_data = load_model()

# =====================
# METRIC
# =====================
c1, c2, c3 = st.columns(3)

c1.metric("📊 Akurasi", f"{accuracy*100:.2f}%")
c2.metric("📁 Total Data", total_data)
c3.metric("🤖 Algoritma", "Decision Tree")

st.info("Akurasi dihitung dari data uji (train-test split)")

# =====================
# SESSION HISTORY
# =====================
if "history" not in st.session_state:
    st.session_state.history = []

# =====================
# MODE
# =====================
mode = st.radio("Mode:", ["Single Image", "Compare 2 Images"])

# =====================
# SINGLE IMAGE
# =====================
if mode == "Single Image":
    file = st.file_uploader("Upload gambar", type=["jpg","png","jpeg"])

    if file:
        img = Image.open(file)
        np_img = np.array(img)

        st.image(img, width=300)

        feat = extract_glcm_features(np_img)
        pred = model.predict([feat])[0]

        # confidence
        proba = model.predict_proba([feat])[0]
        conf = max(proba) * 100

        st.success(f"Hasil Klasifikasi: **{pred}**")
        st.progress(int(conf))
        st.caption(f"Confidence: {conf:.2f}%")

        st.session_state.history.append({
            "File": file.name,
            "Hasil": pred,
            "Confidence (%)": round(conf,2)
        })

        # detail fitur
        with st.expander("🔍 Detail Fitur GLCM"):
            st.write({
                "Contrast": feat[0],
                "Correlation": feat[1],
                "Energy": feat[2],
                "Homogeneity": feat[3],
            })

        # grafik fitur
        df = pd.DataFrame({
            "Fitur": ["Contrast","Correlation","Energy","Homogeneity"],
            "Nilai": feat
        })
        st.bar_chart(df.set_index("Fitur"))

# =====================
# COMPARE MODE
# =====================
if mode == "Compare 2 Images":
    files = st.file_uploader(
        "Upload 2 gambar",
        type=["jpg","png","jpeg"],
        accept_multiple_files=True
    )

    if files and len(files)==2:
        col1, col2 = st.columns(2)

        for col, f in zip([col1,col2], files):
            im = Image.open(f)
            np_im = np.array(im)
            feat = extract_glcm_features(np_im)
            pred = model.predict([feat])[0]

            col.image(im, width=200)
            col.success(pred)

# =====================
# HISTORY
# =====================
st.markdown("### 📜 Riwayat Prediksi")

if len(st.session_state.history)>0:
    df_hist = pd.DataFrame(st.session_state.history)
    st.table(df_hist)

    st.download_button(
        "⬇️ Download ke Excel",
        df_hist.to_csv(index=False),
        "hasil_klasifikasi.csv"
    )
else:
    st.caption("Belum ada riwayat.")

# =====================
# FOOTER
# =====================
st.markdown("""
<hr>
<p style='text-align:center;font-size:12px;color:gray;'>
UAS Computer Vision | GLCM & Decision Tree
</p>
""", unsafe_allow_html=True)
