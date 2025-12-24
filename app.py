import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import io

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(page_title="Confusion Matrix Generator", layout="centered")

# -------------------------------------------------
# ADVANCED UI STYLING
# -------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1f2a, #183947, #1f4e5f);
    color: white;
}

.glass-card {
    background: rgba(255,255,255,0.95);
    color: #000;
    padding: 28px;
    border-radius: 18px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.35);
    backdrop-filter: blur(12px);
    margin-bottom: 40px;
}

h1 {
    text-align: center;
    font-weight: 700;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

.step-badge {
    display: inline-block;
    background: #2563eb;
    color: white;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 14px;
    margin-bottom: 12px;
}

.help-box {
    background: #f8fafc;
    color: #1e293b;
    padding: 14px;
    border-left: 5px solid #2563eb;
    border-radius: 10px;
    margin-bottom: 20px;
}

button[kind="primary"] {
    background: linear-gradient(135deg, #2563eb, #1e40af);
    border-radius: 10px;
    padding: 0.6em 1.2em;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown("<h1>Confusion Matrix Generator</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Clean UI • Clear Row–Column Mapping • Publication-Ready Output</div>",
    unsafe_allow_html=True
)

# -------------------------------------------------
# CARD START
# -------------------------------------------------






# -------------------------------------------------
# STEP 1
# -------------------------------------------------
st.markdown("<div class='step-badge'>Step 1</div>", unsafe_allow_html=True)
st.subheader("Configure Classes")

num_classes = st.number_input("Number of classes", 2, 20, 4, 1)

labels_text = st.text_input(
    "Class names (comma-separated)",
    value=", ".join([f"Class {i+1}" for i in range(num_classes)])
)

labels = [x.strip() for x in labels_text.split(",") if x.strip()]
if len(labels) != num_classes:
    st.error("Number of class names must match number of classes.")
    st.stop()

# -------------------------------------------------
# STEP 2
# -------------------------------------------------
st.markdown("<div class='step-badge'>Step 2</div>", unsafe_allow_html=True)
st.subheader("Enter Confusion Matrix Values")

st.markdown("""
<div class="help-box">
<b>Rows</b> = Actual classes<br>
<b>Columns</b> = Predicted classes<br>
Example: <b>R1 → C2</b> means Actual = Class 1, Predicted = Class 2
</div>
""", unsafe_allow_html=True)

cm = np.zeros((num_classes, num_classes), dtype=int)

header = st.columns(num_classes + 1)
header[0].markdown("**Actual \\ Predicted**")
for j in range(num_classes):
    header[j+1].markdown(f"**C{j+1}<br>{labels[j]}**", unsafe_allow_html=True)

for i in range(num_classes):
    row = st.columns(num_classes + 1)
    row[0].markdown(f"**R{i+1} – {labels[i]}**")
    for j in range(num_classes):
        cm[i, j] = row[j+1].number_input(
            f"R{i+1}→C{j+1}",
            min_value=0,
            step=1,
            key=f"{i}_{j}"
        )

# -------------------------------------------------
# STEP 3
# -------------------------------------------------
st.markdown("<div class='step-badge'>Step 3</div>", unsafe_allow_html=True)
st.subheader("Export Settings")

col1, col2 = st.columns(2)
with col1:
    file_format = st.selectbox("Format", ["PNG", "JPG", "PDF"])
with col2:
    dpi = st.selectbox("DPI", [300, 600])

file_name = st.text_input("File name", "Confusion_Matrix")

# -------------------------------------------------
# GENERATE FUNCTION
# -------------------------------------------------
def generate_confusion_matrix(cm, labels, dpi):
    fig, ax = plt.subplots(figsize=(7,6), dpi=dpi)
    im = ax.imshow(cm, cmap="Blues")
    fig.colorbar(im)

    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_yticklabels(labels)

    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, cm[i,j], ha="center", va="center")

    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("Confusion Matrix")
    plt.tight_layout()
    return fig

# -------------------------------------------------
# GENERATE & DOWNLOAD
# -------------------------------------------------
if st.button("Generate & Download High-Quality Image", type="primary"):
    fig = generate_confusion_matrix(cm, labels, dpi)
    st.pyplot(fig)

    buffer = io.BytesIO()
    ext = file_format.lower()
    fig.savefig(buffer, format=ext if ext != "jpg" else "jpeg", dpi=dpi)
    buffer.seek(0)

    st.download_button(
        "Download Image",
        data=buffer,
        file_name=f"{file_name}.{ext}",
        mime=f"image/{ext}"
    )

    plt.close(fig)

# -------------------------------------------------
# CARD END
# -------------------------------------------------
st.markdown("</div>", unsafe_allow_html=True)
