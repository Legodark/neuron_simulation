import streamlit as st
import numpy as np

from features.neuron import Neuron

st.image('src/images/neuron.jpg')

st.title('Simulacion de neurona')

dentrites = st.slider('Elige el número de entradas/pesos que tendrá la neurona', 1, 10)

st.markdown('### Pesos')

w = []
x = []


col_dentrites = st.columns(dentrites)

for index, col in enumerate(col_dentrites):
    
    
    with col:
        
        titles = index 
        key_name_peso = "p" + str(index)
        
        peso_title = st.markdown(f'$w_{titles}$')
        peso = st.number_input('Introduce un valor', 0.0, 100.0, key=key_name_peso)
        w.append(peso)
        
st.markdown(f'$w$ = {w}')
          
st.markdown('### Entradas')

col_dentrites_2 = st.columns(dentrites)

for index, col in enumerate(col_dentrites_2):
        
    with col:
        
        titles = index
        key_name_value = "v" + str(index)
        
        input_value_title = st.markdown(f'$w_{titles}$')
        input_value = st.number_input('Introduce un valor', key=key_name_value)
        x.append(input_value)
    
st.markdown(f'$x$ = {x}')
    
col1, col2 = st.columns(2)
    
with col1: 
    st.markdown('### Sesgo')
    sesgo = st.number_input('Introduce un valor', key='bias_0')
    
with col2: 
    st.markdown('### Función de activación')
    activation_function = st.selectbox('Elige la función de activación', ['Sigmoide', 'ReLU', 'Tangente hiperbólica'])
    
    
if st.button('Calcular la salida :zap:'):
    # Instanciación de la clase Neuron
    neuron = Neuron(w, sesgo, activation_function)
    output = neuron.run(x)
    st.markdown(f'### La salida de la neurona es {output}')
