# 🏠 House Price Predictor

An end-to-end Machine Learning project that predicts residential property prices using property features such as BHK, area, locality, region, property age, house type, and construction status. The project includes data preprocessing, model comparison, hyperparameter tuning, model evaluation, and deployment through a Streamlit web application.

---

## 📌 Project Overview

Accurate property price estimation is essential for buyers, sellers, investors, and real estate professionals. This project leverages Machine Learning to build a regression model capable of predicting house prices based on multiple property characteristics.

The project follows a complete machine learning workflow—from data preprocessing and feature engineering to model selection, optimization, and deployment.

---

##  Live Demo
link

---

## 🚀 Features

* Predicts residential property prices instantly
* Interactive Streamlit web interface
* Dynamic Region → Locality selection
* Supports multiple house types
* User-friendly input form
* Fast real-time predictions

---

## 📊 Dataset

The dataset contains information about residential properties, including:

* BHK
* Area (Sq. Ft.)
* Region
* Locality
* Property Age
* House Type
* Construction Status
* Target Variable: House Price

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

* Removed duplicate records
* Handled missing values
* Feature selection
* Encoded categorical variables
* Created numerical mappings for Region and Locality
* Prepared deployment dictionaries for Region–Locality relationships
* Train-Test Split

---

## 🤖 Machine Learning Models Evaluated

Several regression algorithms were trained and evaluated:

* Linear Regression
* Lasso Regression
* Ridge Regression
* Decision Tree Regressor
* Random Forest Regressor

Model performance was compared using multiple evaluation metrics before selecting the best-performing model.

---

## ⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed on the Random Forest Regressor using RandomizedSearchCV.

The tuning process optimized parameters such as:

* Number of estimators
* Maximum depth
* Minimum samples split
* Minimum samples leaf
* Bootstrap
* Maximum features

Although hyperparameter tuning produced a slight improvement in prediction accuracy, it also increased the serialized model size significantly.

---

## 📈 Model Performance

### Final Deployed Model

* **Algorithm:** Random Forest Regressor
* **Number of Trees:** 25
* **Mean Absolute Percentage Error (MAPE):** **7.92%**
* **R² Score:** **0.9407**
* **Mean Absolute Error (MAE):** **14.60**

The deployed model was selected after balancing prediction accuracy with deployment efficiency.

### Engineering Decision

The fully tuned Random Forest achieved a slightly lower MAPE but produced a model larger than **1 GB**, making it impractical for deployment.

A carefully optimized Random Forest with **25 estimators** reduced the model size to approximately **85 MB** while maintaining nearly identical predictive performance, making it suitable for deployment on lightweight cloud platforms.

This reflects an important real-world machine learning trade-off between model performance and production constraints.

---

## 📐 Evaluation Metrics

The models were evaluated using:

* Mean Absolute Percentage Error (MAPE)
* Mean Absolute Error (MAE)
* R² Score

---

## 🖥️ Streamlit Application

The project includes a fully interactive Streamlit application where users can:

* Select Region
* Select Locality dynamically
* Enter BHK
* Enter Area
* Choose Property Age
* Choose House Type
* Choose Construction Status
* Predict the estimated property price instantly

Predictions are displayed in:

* **Lakhs** (for prices below ₹1 Crore)
* **Crores** (for prices of ₹1 Crore and above)

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* Git
* GitHub

---

## 📂 Project Structure

```text
House_Price_Predictor/
│
├── app2.py
├── house_price_model.pkl
├── locality_dict.pkl
├── region_dict.pkl
├── region_locality_dict.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 💡 Key Learnings

Through this project, I gained hands-on experience in:

* End-to-end Machine Learning workflow
* Data preprocessing and feature engineering
* Regression model comparison
* Hyperparameter tuning
* Model evaluation and selection
* Model serialization using Pickle
* Building interactive Streamlit applications
* Git and GitHub version control
* Balancing model accuracy with deployment constraints

---

## 🔮 Future Improvements

* Integrate additional property features
* Incorporate geospatial information
* Add model explainability using SHAP
* Deploy on a cloud platform with CI/CD
* Build a REST API for integration with external applications

---

## 👨‍💻 Author

**Sayan Das**

If you found this project interesting, feel free to connect with me on LinkedIn or explore my other repositories.

