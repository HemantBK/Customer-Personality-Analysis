import numpy as np
import pickle
import pandas as pd
import streamlit as st


classifier = pickle.load(open('classifier.pkl','rb'))


#creating a function
# customer segmentation function
def segment_customers(input_data):

 prediction=classifier.predict(pd.DataFrame(input_data, columns=['Income','Kidhome','Teenhome','Age','Partner','Education_Level']))
 print(prediction)
 pred_1 = 0
 if prediction == 0:
     pred_1 = 'cluster 0'

 elif prediction == 1:
     pred_1 = 'cluster 1'

 elif prediction == 2:
    pred_1 = 'cluster 2'

 elif prediction == 3:
     pred_1 = 'cluster 3'
        
 elif prediction == 4:
     pred_1 = 'cluster 4'

 return pred_1

st.title('Customer Personality Analysis')

st.header('User Input Parameters')
def main():
    
    Income = st.number_input("Type In The Household Income")
    Kidhome = st.radio ( "Select Number Of Kids In Household", ('0', '1','2') )
    Teenhome = st.radio ( "Select Number Of Teens In Household", ('0', '1','2') )
    Age = st.slider ( "Select Age", 18, 85 )
    st.write("Customer Age is", Age)
    Partner = st.radio ( "Married?", ('Yes', 'No') )
    Education_Level = st.radio ( "Select Education", ("Undergraduate", "Graduate", "Postgraduate") )
   
    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Segment Customer"):
        result=segment_customers([[Income,Kidhome,Teenhome,Age,Partner,Education_Level]])
    
    st.success(result)
    

if __name__ == '__main__':
        main ()