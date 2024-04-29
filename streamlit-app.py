import streamlit as st
import joblib

# Load your trained model
phish_model = joblib.load('phishing.pkl')

def predict_phishing(features):
    X_predict = [str(features)]
    y_Predict = phish_model.predict(X_predict)
    if y_Predict == 'bad':
        return "This is a Phishing Site"
    else:
        return "This is not a Phishing Site"

# Streamlit user interface
st.title('Phishing Detection App')
user_input = st.text_input("Enter the URL features to predict if it's a phishing site:")

if st.button('Predict'):
    result = predict_phishing(user_input)
    st.write(f"The site with features is predicted as: {result}")
