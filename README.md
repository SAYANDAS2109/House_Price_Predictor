# 🏠 House Price Predictor

An end-to-end Machine Learning project that predicts residential property prices using property characteristics such as **BHK, area, locality, region, property age, house type, and construction status**.

This project demonstrates the complete Machine Learning pipeline, including data preprocessing, feature engineering, feature encoding, model comparison, hyperparameter tuning, evaluation, deployment optimization, and an interactive Streamlit web application.

---

# 🌐 Live Demo

🚀 **Streamlit Application**

> **Link:** *https://housepricepredictor-vurfcauat8bjbt3qxdtppg.streamlit.app/*



---

# 📌 Project Overview

Estimating residential property prices accurately is one of the most important problems in the real estate industry.

This project applies supervised machine learning techniques to build a predictive model capable of estimating house prices based on multiple property features.

The project follows a complete end-to-end workflow:

* Data Cleaning
* Data Preprocessing
* Feature Engineering
* Feature Encoding
* Model Training
* Model Comparison
* Hyperparameter Tuning
* Model Evaluation
* Model Selection
* Model Serialization
* Streamlit Deployment

---

# 🚀 Features

* Interactive Streamlit Interface
* Real-time House Price Prediction
* Dynamic Region → Locality Selection
* Supports Multiple House Types
* User-Friendly Interface
* Instant Price Prediction
* Displays prices in Lakhs or Crores automatically
* Production-ready Machine Learning Model

---

# 📊 Dataset

The dataset contains residential property information including:

* BHK
* Area (Sq. Ft.)
* Region
* Locality
* Property Age
* House Type
* Construction Status
* House Price (Target Variable)

---

# 🧹 Data Preprocessing

Several preprocessing techniques were applied before model training.

### ✔ Duplicate Removal

Duplicate property records were removed.

### ✔ Missing Value Handling

Missing values were identified and removed from the dataset.

### ✔ Data Cleaning

Unnecessary columns were removed.

Categorical values were standardized.

### ✔ Feature Selection

Only relevant features were selected for training.

---

# ⚙ Feature Engineering & Encoding

Several feature engineering techniques were implemented.

## Numerical Features

* Area
* BHK

## Encoded Features

Categorical variables were converted into numerical values.

### Label Encoding

Used for:

* Region
* Locality
* Property Age

Separate encoding dictionaries were created and saved for deployment.

Examples:

* `region_dict.pkl`
* `locality_dict.pkl`

---

### One-Hot Encoding using pd.get_dummies()

Applied to:

House Type

* Apartment
* Studio Apartment
* Villa
* Other

Construction Status

* Ready to Move
* Under Construction

---

### Dynamic Region–Locality Mapping

A custom Region → Locality dictionary was created.

This enables:

* Selecting a region first.
* Automatically displaying only the localities belonging to that region.

This significantly improves the usability of the Streamlit application.

---

# 🤖 Machine Learning Models Evaluated

Multiple regression algorithms were trained and compared.

Models evaluated:

* Linear Regression
* Lasso Regression
* Ridge Regression
* Decision Tree Regressor
* Random Forest Regressor

The models were compared based on prediction accuracy and evaluation metrics.

---

# ⚙ Hyperparameter Tuning

Hyperparameter optimization was performed using **RandomizedSearchCV**.

The following parameters were optimized:

* Number of Estimators
* Maximum Depth
* Bootstrap
* Minimum Samples Split
* Minimum Samples Leaf
* Maximum Features

The tuned model achieved the best prediction accuracy but produced a model larger than **1 GB**, making it unsuitable for deployment.

---

# 📈 Model Evaluation

The models were evaluated using:

* Mean Absolute Percentage Error (MAPE)
* Mean Absolute Error (MAE)
* R² Score

---

# 🏆 Final Deployed Model

After evaluating multiple models, **Random Forest Regressor** achieved the best performance.

### Final Deployment Configuration

* Algorithm: Random Forest Regressor
* Trees: **25**
* Model Size: **~85 MB**

### Performance

* **MAPE:** **7.92%**
* **R² Score:** **0.9407**
* **MAE:** **14.60**

---

# 💡 Deployment Optimization

Although hyperparameter tuning slightly improved prediction accuracy, the resulting model exceeded **1 GB**.

To make the application deployable while maintaining excellent performance, the number of trees was reduced to **25**, resulting in:

* Significant reduction in model size
* Nearly identical prediction accuracy
* Faster loading time
* Easier deployment

This demonstrates an important real-world engineering trade-off between model performance and production constraints.

---

# 🖥 Streamlit Application

The project includes an interactive Streamlit web application.

Users can:

* Select Region
* Select Locality
* Enter Area
* Enter BHK
* Select Property Age
* Select House Type
* Select Construction Status
* Predict House Price instantly

The application automatically displays:

* Prices below ₹1 Crore in **Lakhs**
* Prices above ₹1 Crore in **Crores**

---

# 📁 Project Structure

```text
House_Price_Predictor/
│
├── app2.py
├── house_price_model(4).pkl
├── locality_dict(1).pkl
├── region_dict(1).pkl
├── region_locality_dict(1).pkl
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
```

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* Git
* GitHub

---

# ▶ Installation

Clone the repository

```bash
git clone https://github.com/SAYANDAS2109/House_Price_Predictor.git
```

Move into the project directory

```bash
cd House_Price_Predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app2.py
```

---

# 📚 Key Learnings

This project provided practical experience in:

* Data Cleaning
* Data Preprocessing
* Feature Engineering
* Feature Encoding
* Regression Algorithms
* Model Comparison
* Hyperparameter Tuning
* Model Evaluation
* Model Serialization using Pickle
* Building Interactive Streamlit Applications
* Git Version Control
* GitHub Repository Management
* Model Deployment
* Production Model Optimization

---

# 🔮 Future Improvements

* Add more property features
* Develop a REST API
* Explore Gradient Boosting and XGBoost for further performance improvements

---

# 👨‍💻 Author

**Sayan Das**

Feel free to connect with me on LinkedIn and explore my other Machine Learning projects.
https://www.linkedin.com/in/sayan-das-1466b1369/

---



