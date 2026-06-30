# 🏠 Mumbai House Price Prediction using Machine Learning

An end-to-end Machine Learning application that predicts residential property prices across Mumbai based on property characteristics such as location, area, BHK configuration, property age, construction status, and property type.

The project covers the complete Machine Learning lifecycle, including data preprocessing, feature engineering, model selection, hyperparameter optimization, evaluation, and deployment through an interactive Streamlit web application.

---

## 🚀 Live Demo

🔗 **Streamlit App:** *(Add your deployed Streamlit URL here)*

---

## 📌 Project Overview

Buying a property involves evaluating numerous factors that influence its market value. This project aims to assist buyers, sellers, and real estate enthusiasts by providing accurate house price predictions using supervised Machine Learning.

The application allows users to enter property details through an intuitive interface and instantly receive an estimated property price.

---

# ✨ Features

- 🏙️ Dynamic Region → Locality Selection
- 🏠 Property Type Selection
- 🛏️ BHK Selection
- 📐 Area Input
- 🏗️ Construction Status Selection
- 🕒 Property Age Selection
- 💰 Automatic Price Formatting (Lakhs / Crores)
- ⚡ Real-time Predictions
- 📊 Interactive Streamlit Interface

---

# 📂 Dataset

The dataset contains residential property listings from Mumbai and includes features such as:

- BHK
- Area (Sq.ft)
- Region
- Locality
- Property Age
- Property Type
- Construction Status
- Property Price (Target Variable)

---

# 🛠 Data Preprocessing

Several preprocessing steps were performed before training the models.

### ✔ Data Cleaning

- Removed duplicate entries
- Removed missing values
- Standardized categorical values
- Handled inconsistent location names

### ✔ Feature Engineering

- Target Encoding for:
  - Region
  - Locality

- One-Hot Encoding for:
  - Property Type
  - Construction Status

- Numerical Encoding for:
  - Property Age

---

# 🤖 Machine Learning Models Evaluated

Multiple regression algorithms were trained and evaluated to identify the best-performing model.

### Models Tested

- Linear Regression
- Lasso Regression
- Ridge Regression
- Decision Tree Regressor
- Random Forest Regressor

Each model was evaluated using standard regression metrics.

---

# 🎯 Model Selection

After comparing the performance of all trained models, **Random Forest Regressor** consistently produced the highest predictive accuracy and generalization performance.

Therefore, it was selected as the final production model.

---

# ⚙ Hyperparameter Tuning

To further improve performance, **RandomizedSearchCV** was used to optimize the Random Forest model.

### Tuned Parameters

- Number of Estimators
- Maximum Depth
- Maximum Features
- Minimum Samples Split
- Minimum Samples Leaf
- Bootstrap

The optimized model significantly improved prediction accuracy while reducing overfitting.

---

# 📈 Model Performance

| Metric | Score |
|---------|-------|
| R² Score | **0.945** |
| Mean Absolute Error (MAE) | **14.35 Lakhs** |
| Mean Absolute Percentage Error (MAPE) | **7.9%** |

These results demonstrate that the model is capable of providing highly accurate price estimates on unseen data.

---

# 💻 Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

### Development Environment

- Google Colab
- Visual Studio Code
- Git
- GitHub

---

# 🌐 Web Application

The trained model has been deployed using **Streamlit**.

The web application allows users to:

- Select Region
- Select Locality
- Enter Area
- Select Property Age
- Select Property Type
- Select Construction Status
- Predict Property Price

The application automatically performs feature encoding before passing the data into the trained model.

---

# 📁 Project Structure

```
Mumbai-House-Price-Prediction
│
├── app.py
├── house_price_model.pkl
├── locality_dict.pkl
├── region_dict.pkl
├── region_locality_dict.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

# 📷 Application Preview

## Home Page

*(Insert Screenshot)*

---

## Prediction Result

*(Insert Screenshot)*

---

# 🔄 Machine Learning Workflow

```
Dataset
    │
    ▼
Data Cleaning
    │
    ▼
Feature Engineering
    │
    ▼
Encoding
    │
    ▼
Train-Test Split
    │
    ▼
Model Training
    │
    ▼
Model Comparison
    │
    ▼
Random Forest Selection
    │
    ▼
Hyperparameter Tuning
    │
    ▼
Model Evaluation
    │
    ▼
Model Serialization (.pkl)
    │
    ▼
Streamlit Deployment
```

---

# 🚀 Future Improvements

- Google Maps Integration
- Price Trend Visualization
- Property Recommendation System
- User Authentication


---

# 👨‍💻 Developer

## Sayan Das

### Connect with me

- GitHub: https://github.com/yourusername
- LinkedIn: https://linkedin.com/in/yourprofile

---

## 📜 License

This project is licensed under the **MIT License**.
