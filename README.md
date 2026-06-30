# Disease-Prediction-System

A Machine Learning-based web application that predicts whether a patient is at risk of heart disease using clinical and medical parameters. This project compares multiple classification algorithms and selects the best-performing model for deployment with Streamlit.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help in timely diagnosis and treatment.

This project uses machine learning techniques to analyze patient medical data and predict the likelihood of heart disease.

---

## 🎯 Objectives

- Perform data preprocessing and exploratory data analysis (EDA).
- Train multiple machine learning classification models.
- Compare model performance using evaluation metrics.
- Save the best-performing model.
- Build an interactive Streamlit application for prediction.

---

## 📂 Dataset

**Dataset:** Heart Disease UCI Dataset

The dataset contains **302 unique patient records** with the following features:

| Feature | Description |
|----------|-------------|
| age | Age of the patient |
| sex | Gender (0 = Female, 1 = Male) |
| cp | Chest pain type |
| trestbps | Resting blood pressure |
| chol | Serum cholesterol |
| fbs | Fasting blood sugar |
| restecg | Resting electrocardiographic results |
| thalach | Maximum heart rate achieved |
| exang | Exercise induced angina |
| oldpeak | ST depression induced by exercise |
| slope | Slope of the peak exercise ST segment |
| ca | Number of major vessels |
| thal | Thalassemia |
| target | Heart disease (0 = No, 1 = Yes) |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Pickle

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

- Dataset overview
- Missing value analysis
- Duplicate removal
- Target distribution
- Age distribution
- Gender distribution
- Chest pain analysis
- Cholesterol distribution
- Blood pressure distribution
- Correlation heatmap
- Outlier detection

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- XGBoost

---

## 📈 Model Evaluation

Models were compared using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score

### Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | **80.33%** |
| Decision Tree | **80.33%** |
| SVM | 77.05% |
| Random Forest | 75.41% |
| XGBoost | 72.13% |

**Best Model:** Logistic Regression

---

## 🚀 Streamlit Application

The web application allows users to enter:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression
- Slope
- Number of Major Vessels
- Thalassemia

The application predicts whether the patient is likely to have heart disease and displays the prediction probability.

---


## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Heart-Disease-Prediction.git
```

Move into the project directory:

```bash
cd Heart-Disease-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

## 📌 Future Improvements

- Hyperparameter tuning using GridSearchCV
- Cross-validation
- Feature selection
- SHAP explainability
- Cloud deployment
- Real-time prediction API

---

## 👨‍💻 Author

**Shweta Singh**

Computer Science Student

---
