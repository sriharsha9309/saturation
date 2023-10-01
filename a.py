import streamlit as st
import pickle

# Load the trained model from the pickle file
spo2=pickle.load(open("F:\spo2\spo2.pkl", 'rb'))


# Create the Streamlit app
st.title('Transcutaneous oxygen saturation prediction')
st.write('This app predicts transcutaneous oxygen saturation (TcPO2) basing on the patient record.')
st.write('TcPO2 is a measure of the amount of oxygen in the tissue below the skin. It can be used to assess blood flow and tissue perfusion.')
st.write('Enter the following features for the prediction:')

age = st.sidebar.number_input('Enter your age: ')
BMI=st.sidebar.number_input('Enter your BMI: ')
diabetes=st.sidebar.selectbox('diabetes', ("Yes","No"))
s_bp=st.sidebar.number_input('Enter your Systolic BP: ')
d_bp=st.sidebar.number_input('Enter your Diastolic BP: ')
resp=st.sidebar.number_input('Enter your Respiratory rate: ')
hrate=st.sidebar.number_input('Enter your heart rate : ')

# Create a button to make the prediction
if st.button('Make Prediction'):
    # Make the prediction using the input values
    features = [[age,BMI,diabetes,s_bp,d_bp,resp, hrate]]
    if(diabetes=="Yes"):
        diabetes=1
    else:
        diabetes=0
    result = spo2.predict(features)[0]

    # Display the prediction
    st.write('Predicted TcPO2:', result)
