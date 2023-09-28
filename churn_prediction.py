# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:46:30 2023

@author: KIIT
"""

import numpy as np
import pickle
import streamlit as st

#Loading The Model 
loaded_model=pickle.load(open('D:/Internship/model.sav','rb'))

def churn_prediction(input_data):
    #changing the input to numpy array
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    predicition=loaded_model.predict(input_data_reshaped)
    print(predicition)
    if(predicition[0]==0):
        return 'The Customer Is Not Likely To Churn'
    else:
        return 'The Customer Is Likely To Churn'
    
    
def main():
    #Giving The Title 
    
    st.title('Churn Prediction')
    
    #getting The Input Data From user 
    Age=st.text_input('Age Of The Person')
    Gender=st.text_input('Gender Of The Person')
    Location=st.text_input('Location Of The Person')
    Subscription_Length_Months=st.text_input('Number Of Subscription Month')
    Monthly_Bill=st.text_input('Monthly Bill')
    Total_Usage_GB=st.text_input('Total Usage GB')             
    
    #code for prediciton
    diagonsis=''

    #creating a button for prediction
    if st.button('Churn Prediciton Result'):
        diagonsis=churn_prediction([Age,Gender,Location,Subscription_Length_Months,Monthly_Bill,Total_Usage_GB])
        
        
        
    st.success(diagonsis)
    
    
if __name__=='__main__':
    main()
    
