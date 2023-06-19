# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 14:50:06 2023

@author: ruben
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
import joblib

classifier = pickle.load(open('bestmodelSVC.pkl', 'rb'))
st.set_page_config(layout="wide")




#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(battery_power,fc,int_memory,mobile_wt,px_height,px_width,ram,sc_w,talk_time):
    
    """Variáveis a utilizar.
    ---
    parameters:  
      - battery_power
      - blue
      - clock_speed
      - dual_sim
      - fc
      - four_g
      - int_memory
      - m_dep
      - mobile_wt
      - n_cores
      - pc
      - px_height
        px_width
        ram
        sc_h
        sc_w
        talk_time
        three_g
        touch_screen
        wifi
            intervalo de preços: output
        
    """
    

   
    prediction=classifier.predict([[battery_power,fc,int_memory,mobile_wt,px_height,px_width,ram,sc_w,talk_time]])
    print(prediction)
    return prediction



def main():
    st.image('logo.png', width=1200)
    st.title("Classificador Telemoveis")

    with st.sidebar:
        st.image('header.png', width=200)
        battery_power = st.number_input("Qual a autonomia?(em mAh))",1 )
        
        chooseBat = st.selectbox('Tem Camera Frontal?', ('Sim', 'Nao'))
        if chooseBat == 'Sim':
            fc = 1
        else:
            fc = 0

        int_memory = st.number_input("Qual a capacidade de armazenamento? (em GB)", 1) #importa
        ram = st.number_input("Quantidade de Memória RAM? (em GB)",1)
        talk_time = st.number_input("Duração da bateria em funcionamento? (em h)",1 )    
        
        st.header("Caracteristicas Fisicas")
        
        px_height = st.number_input("Resolução-Altura de Ecran? (em pixeis)") #importa
        px_width = st.number_input("Resolução-Largura (em pixeis)")
        mobile_wt = st.number_input("QPeso? (em g)") #importa
        sc_w = st.number_input("Largura do Telemovel (em cm)")
        
        
    
    result=""
    
    
    if st.button("Predict"):
        result=predict_note_authentication(battery_power,fc,int_memory,mobile_wt,px_height,px_width,ram,sc_w,talk_time)
    
    if result == 0:
        st.success('O telemovel está na classe de Baixo Preço')
        
    if result == 1:
        st.success('O telemovel está na classe de Preço Médio')
    if result == 2:
        st.success('O telemovel está na classe de Preço Alto')
    if result == 3:
        st.success('O telemovel está na classe de Preço Muito Alto')
        
        
    if st.button("Infos"):
        st.text("V.16 - Classificador de Telemoveis, Ruben Marques")
        st.text("")

if __name__=='__main__':
    main()
    
    