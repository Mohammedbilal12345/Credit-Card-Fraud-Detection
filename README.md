# Credit Card Fraud Detection Using Machine Learning & Streamlit

![Python](https://img.shields.io/badge/python-v3.11-blue?logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-v1.24-orange?logo=streamlit\&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-v1.2-green?logo=scikitlearn\&logoColor=white)

---

## 📌 Project Overview

Credit card fraud is a significant concern in the financial sector, leading to millions of dollars in losses every year. This project demonstrates how machine learning can be used to **detect fraudulent credit card transactions** in real-time.

The solution utilizes a **Logistic Regression** model trained on a balanced dataset, and a user-friendly **Streamlit** web application that allows users to input transaction details and instantly predict if a transaction is legitimate or fraudulent.

---

## 🚀 Features

* **Data balancing:** Handles class imbalance via undersampling to improve model fairness.
* **Accurate predictions:** Logistic Regression model trained and tested with high accuracy.
* **Real-time UI:** Interactive Streamlit interface for entering transaction data and viewing results.
* **Visual feedback:** Engaging animations and alerts for clear fraud notifications.
* **Lightweight:** Uses only essential libraries to keep the app fast and responsive.

---

## 🗂️ Dataset

The dataset used is the **Credit Card Fraud Detection Dataset** from Kaggle:

* **Source:** [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
* **Description:** Contains transactions made by European cardholders over two days in September 2013.
* **Size:** 284,807 transactions, including 492 frauds (\~0.17%).
* **Features:** 30 anonymized numeric features (V1, V2, ..., V28, plus `Time` and `Amount`).
* **Target:** `Class` — 0 for legitimate, 1 for fraud.

---

## 📊 Machine Learning Pipeline

1. **Data Loading:** Load the CSV dataset using Pandas.
2. **Data Balancing:** Undersample the majority class to balance the dataset.
3. **Feature Preparation:** Separate features (X) and target (y).
4. **Train-Test Split:** Stratified split into 80% training and 20% testing data.
5. **Model Training:** Logistic Regression model with `max_iter=1000`.
6. **Model Evaluation:** Calculate training and testing accuracy.
7. **Prediction:** Real-time input from users via Streamlit and model inference.

---

## 🛠️ Installation

Make sure you have Python 3.7+ installed.

```bash
# Clone the repo
git clone https://github.com/Mohammedbilal12345/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚩 Usage

To run the Streamlit app locally:

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501` to access the app.

---

## ⚙️ App Functionality

* Enter comma-separated transaction data with 30 features.
* Click **Submit** to get instant fraud prediction.
* Legitimate transactions show a confetti animation and a positive message.
* Fraudulent transactions display an alert, sound, and warning visuals.

---

## 📈 Results

| Metric            | Value    |
| ----------------- | -------- |
| Training Accuracy | \~XX.XX% |
| Testing Accuracy  | \~XX.XX% |

> *Note: Actual accuracy values depend on the data split and training.*

---

## 🧑‍💻 Technologies Used

* Python 3.11
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* HTML, CSS (for custom animations)

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📚 References

* [Kaggle Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
* [Streamlit Documentation](https://docs.streamlit.io/)
* [Scikit-learn Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

---

### Made with ❤️ by Mohammed Bilal

