import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st
import streamlit.components.v1 as components

# Load data
data = pd.read_csv('creditcard.csv')
legit = data[data['Class'] == 0]
fraud = data[data['Class'] == 1]

# Undersample to balance classes
legit_sample = legit.sample(n=len(fraud), random_state=2)
data = pd.concat([legit_sample, fraud], axis=0)

# Prepare features and labels
X = data.drop(columns="Class", axis=1)
y = data["Class"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=4)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

train_acc = accuracy_score(y_train, model.predict(X_train))
test_acc = accuracy_score(y_test, model.predict(X_test))

# Streamlit app UI
st.set_page_config(page_title="Fraud Detector", layout="centered")
st.title("💳 Credit Card Fraud Detection")
st.markdown("Enter transaction data to detect fraud in real-time.")

st.write(f"**📈 Training Accuracy:** `{train_acc:.2f}`")
st.write(f"**📊 Testing Accuracy:** `{test_acc:.2f}`")

input_df = st.text_input(f"🔍 Enter transaction data (comma-separated, {X.shape[1]} features):", "")

submit = st.button("🚀 Submit")

if submit:
    try:
        input_df_splited = input_df.split(',')
        features = np.asarray(input_df_splited, dtype=np.float64)

        if features.shape[0] != X.shape[1]:
            st.error(f"⚠️ Expected {X.shape[1]} features, but got {features.shape[0]}.")
        else:
            prediction = model.predict(features.reshape(1, -1))

            if prediction[0] == 0:
                st.success("✅ Transaction is Legitimate")

                # 🎉 Confetti animation + celebration sound + happy gif
                components.html(
                    """
                    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                    <script>
                    confetti({
                      particleCount: 150,
                      spread: 90,
                      origin: { y: 0.6 }
                    });
                    </script>
                    <audio autoplay>
                      <source src="https://actions.google.com/sounds/v1/cartoon/clang_and_wobble.ogg" type="audio/ogg">
                      Your browser does not support the audio element.
                    </audio>
                    <div style="text-align:center; margin-top:20px;">
                        <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDdnZG5kdHFrZGJwNWE4dThhZ29seXN0MGs0YmppYmdnY2Y5Zm82ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/111ebonMs90YLu/giphy.gif" width="300" alt="Safe Transaction">
                    </div>
                    """,
                    height=300,
                )

            else:
                st.error("❌ Transaction is Fraudulent")

                # 🔴 Red blinking alert + warning sound + hacker gif
                st.markdown("""
                <div style="
                    padding:20px; 
                    border: 4px solid red; 
                    color: white; 
                    background-color: #ff4b4b; 
                    font-weight: bold; 
                    font-size: 22px; 
                    text-align:center; 
                    animation: blink 1s linear infinite;
                    margin-bottom: 10px;
                    ">
                    ⚠️ FRAUD ALERT! Transaction Denied!
                </div>
                <style>
                @keyframes blink {
                    0% {opacity: 1;}
                    50% {opacity: 0.3;}
                    100% {opacity: 1;}
                }
                </style>
                """, unsafe_allow_html=True)

                components.html(
                    """
                    <audio autoplay>
                        <source src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg" type="audio/ogg">
                        Your browser does not support the audio element.
                    </audio>
                    <div style="text-align:center;">
                        <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjVhYXB4NGUwaDlhYzZ2Y3J5emI4dXAzNWFxcjNxMHpuZjhzcGFuNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hgjNPEmAmpCMM/giphy.gif" width="300" alt="Fraud Alert Hacker">
                    </div>
                    """,
                    height=300,
                )

    except ValueError:
        st.error("⚠️ Please enter valid numeric values separated by commas.")  