import streamlit as st
import pandas as pd
import joblib



# PAGE CONFIGURATION


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)



# TITLE


st.title("📊 Customer Churn Prediction App")

st.write(
    "This app predicts whether a customer will churn "
    "and estimates their churn risk based on their features."
)



# LOAD MODEL


model = joblib.load("churn1.pkl")



# CUSTOMER DETAILS


st.subheader("👤 Customer Details")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )


with col2:

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=72,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )



# SERVICES


st.subheader("🌐 Services")

col1, col2 = st.columns(2)

with col1:

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )


with col2:

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )



# BILLING INFORMATION


st.subheader("💳 Billing Information")

col1, col2 = st.columns(2)

with col1:

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


with col2:

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0
    )



# CREATE DATAFRAME FOR MODEL


input_data = pd.DataFrame({

    "gender": [gender],

    "SeniorCitizen": [senior_citizen],

    "Partner": [partner],

    "Dependents": [dependents],

    "tenure": [tenure],

    "PhoneService": [phone_service],

    "MultipleLines": [multiple_lines],

    "InternetService": [internet_service],

    "OnlineSecurity": [online_security],

    "OnlineBackup": [online_backup],

    "DeviceProtection": [device_protection],

    "TechSupport": [tech_support],

    "StreamingTV": [streaming_tv],

    "StreamingMovies": [streaming_movies],

    "Contract": [contract],

    "PaperlessBilling": [paperless_billing],

    "PaymentMethod": [payment_method],

    "MonthlyCharges": [monthly_charges],

    "TotalCharges": [total_charges]
})



# PREDICTION


st.divider()

if st.button("🔮 Predict Churn"):

    # Prediction
    prediction = model.predict(input_data)[0]

    # Probability of Churn
    churn_probability = model.predict_proba(input_data)[0][1]

    # Convert to percentage
    risk_percentage = churn_probability * 100


   
    # PREDICTION RESULT
    

    if prediction == 1:

        st.error(
            "⚠️ The customer is likely to churn."
        )

    else:

        st.success(
            "✅ The customer is not likely to churn."
        )


    
    # CHURN RISK
    

    st.subheader("📊 Churn Risk")

    st.progress(churn_probability)

    st.write(
        f"Estimated churn risk: **{risk_percentage:.2f}%**"
    )


    
    # RISK CATEGORY
    

    if risk_percentage < 30:

        st.success("🟢 Low Risk")

    elif risk_percentage < 60:

        st.warning("🟡 Medium Risk")

    else:

        st.error("🔴 High Risk")