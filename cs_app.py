import numpy as np
import pickle
import pandas as pd
import streamlit as st

classifier = pickle.load(open('final_model.pkl', 'rb'))

# Creating a function
# Customer segmentation function
def segment_customers(input_data):
    # Prepare the input data for prediction
    encoded_data = [input_data[0], input_data[1], input_data[2], input_data[3], input_data[4], input_data[5],
                    input_data[6], input_data[7]]

    prediction = classifier.predict(pd.DataFrame([encoded_data], columns=['Income', 'NumWebVisitsMonth', 'Age',
                                                                          'Children', 'MntTotalProducts',
                                                                          'NumTotalPurchases', 'Education',
                                                                          'Marital_Status_Married']))

    pred_1 = ""

    if prediction[0] == 0:  # Access the first element of the prediction array
        pred_1 = 'cluster 0'
    elif prediction[0] == 1:
        pred_1 = 'cluster 1'
    elif prediction[0] == 2:
        pred_1 = 'cluster 2'
    elif prediction[0] == 3:
        pred_1 = 'cluster 3'
    elif prediction[0] == 4:
        pred_1 = 'cluster 4'

    return pred_1

st.title('Customer Personality Analysis')

st.header('User Input Parameters')
def main():
    Income = st.number_input("Type In The Household Income", key="income")
    NumWebVisitsMonth = st.number_input("Number of visits to company’s website in the last month", key="num_visits")
    Age = st.slider("Select Age", 18, 85, key="age")
    st.write("Customer Age is", Age)
    Children = st.radio("Select Number Of Children", ('0', '1', '2'))
    MntTotalProducts = st.number_input("Total Amount spent", key="mtp")
    NumTotalPurchases = st.number_input("Number of total purchases", key="ntp")
    Education = st.radio("Select Education", ("Undergraduate", "Graduate", "Postgraduate"))
    Marital_Status_Married = st.radio("Married?", ('No', 'Yes'))

    # Convert selected values to corresponding numerical values
    education_mapping = {'Undergraduate': 2, 'Graduate': 0, 'Postgraduate': 1}
    marital_status_mapping = {'No': 0, 'Yes': 1}

    Education = education_mapping[Education]
    Marital_Status_Married = marital_status_mapping[Marital_Status_Married]

    result = ""

    # When 'Segment Customer' is clicked, make the prediction and store it
    if st.button("Segment Customer"):
        input_data = [Income, NumWebVisitsMonth, Age, Children, MntTotalProducts, NumTotalPurchases,
                      Education, Marital_Status_Married]
        result = segment_customers(input_data)

    st.success(result)


if __name__ == '__main__':
    main()
