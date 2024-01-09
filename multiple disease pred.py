# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:54:13 2024

@author: simran
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabetes_model=pickle.load(open('C:/Users/simran/Desktop/projects-ml/Multiple-disease/saved_model/diabetes_model.sav','rb'))
heart_disease_model=pickle.load(open('C:/Users/simran/Desktop/projects-ml/Multiple-disease/saved_model/Heart-disease_model.sav','rb'))

st.title("Multiple Disease Prediction System")

#sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetic Prediction',
                            'Heart Disease Prediction'
                            ],
                           default_index=0)