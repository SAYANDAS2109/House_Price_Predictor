import streamlit as st
import pandas as pd
import pickle as pkl

model = pkl.load(open("house_price_model (4).pkl","rb"))

locality_dict = pkl.load(open("locality_dict (1).pkl","rb"))

region_dict = pkl.load(open("region_dict (1).pkl","rb"))
region_locality_dict = pkl.load(open("region_locality_dict (1).pkl","rb"))

st.set_page_config(
    page_title= 'HOUSE PRICE PREDICTOR',
    page_icon="🏘️",
    layout='wide',
    initial_sidebar_state="expanded"
)

st.sidebar.image(
    "https://img.icons8.com/color/96/home.png",

     width=80
)



st.sidebar.title("House Price Prediction")

st.sidebar.markdown("---")

st.sidebar.subheader("About")

st.sidebar.write("""
This application estimates residential property prices across Mumbai using a Machine Learning model trained on historical housing data.

Users can enter key property details such as location, area, BHK, property type, age, and construction status to receive an estimated market price.

The project demonstrates the complete Machine Learning workflow—from data preprocessing and feature engineering to model training, hyperparameter tuning, and deployment using Streamlit.
""")

st.sidebar.markdown("---")

st.sidebar.subheader("DEVELOPER")
st.sidebar.write("""
**Sayan Das**


""")


st.title("HOUSE PRICE PREDICTOR")

st.markdown("""
Predict the estimated selling price of residential properties using a trained
**Random Forest Regressor**.

Enter the property details below and click **Predict Price**.
""")

st.divider()

st.subheader("Property Details")

col1 , col2 = st.columns(2)

with col1:

    bhk = st.number_input(
        "BHK",
        min_value=1,
        max_value=10,
        value=2
    )

    area = st.number_input(
        "AREA (Sq.ft)",
        min_value=100,
        value=800
    )

    age = st.selectbox(
        "Property Age",
        ["New","Resale","Unknown"]
    )

    region_display = st.selectbox(
        "Region",
        sorted(region_locality_dict.keys())
    )

with col2:

    house_type = st.selectbox(
        "House Type",
        ["Apartment","Studio Apartment","Villa","Other"]
    )

    status = st.selectbox(
        "Status",
        ["Ready to Move","Under Construction"]
    )

    locality_display = st.selectbox(
        "locality",
        region_locality_dict[region_display]
    )

st.divider()

age_mapping = {
    "New" : 0,
    "Resale" : 1,
    "Unknown":2
}

age = age_mapping[age]

region_key = region_display.lower().replace(" ","")

locality_key = locality_display.lower().replace(" ","")

region_encoded = region_dict[region_key]
locality_encoded = locality_dict[locality_key]

type_apartment = 1 if house_type == "Apartment" else 0
type_other = 1 if house_type == "Other" else 0
type_studio = 1 if house_type == "Studio Apartment" else 0
type_villa = 1 if house_type == "Villa" else 0

status_ready = 1 if status == "Ready to move" else 0
status_under = 1 if status == "Under Construction" else 0

predict = st.button(
    "PREDICT HOUSE PRICE",
    use_container_width=True
)

if predict:

    input_data = pd.DataFrame({
        "bhk": [bhk],
        "locality": [locality_encoded],
        "area": [area],
        "region": [region_encoded],
        "age": [age],
        "type_Apartment": [type_apartment],
        "type_Other": [type_other],
        "type_Studio Apartment": [type_studio],
        "type_Villa": [type_villa],
        "status_Ready to move": [status_ready],
        "status_Under Construction": [status_under]
    })

    prediction = model.predict(input_data)

    predicted_price = prediction[0]

if predict:

    st.divider()

    st.markdown(
        """
        <h2 style='text-align:center;color:#2E86C1;'>
        🎉 Prediction Successful
        </h2>
        """,
        unsafe_allow_html=True
    )
    if predicted_price >= 100:
        formatted_price = f"₹ {predicted_price / 100:.2f} Cr"
    else:
        formatted_price = f"₹ {predicted_price:.2f} Lakhs"

    st.metric(
        label="Estimated House Price",
        value=formatted_price
    )

    st.subheader("Property Summary")

    c1,c2 = st.columns(2)

    with c1:

        st.info(f"""
🏠 **Region:** {region_display}

🏘️ **Locality:** {locality_display}

🛏️ **BHK:** {bhk}

📐 **Area:** {area} sq.ft
""")

    with c2:

        st.info(f"""
🏢 **Property Type:** {house_type}

🏡 **Age:** {age}

🚧 **Status:** {status}
""")
        

st.warning("""
The predicted price is generated using a Machine Learning model
trained on Mumbai housing data.

Actual market prices may vary depending on market conditions.
""")
    
