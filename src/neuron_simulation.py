import streamlit as st

from features.neuron import Neuron

st.image('src/images/neuron.jpg')

st.title('Simulacion de neurona')
st.markdown('###### (v.0.1)')

# Guardo en dentrites el numero de entradas/pesos que quiero tener
dentrites = st.slider('Elige el número de entradas/pesos que tendrá la neurona', 1, 10)

st.markdown('### Pesos')

# Listas para almacenar tanto los pesos como los valores de entreda (input)
w = []
x = []

# Columna donde se generan los pesos
col_dentrites = st.columns(dentrites)

# Con este for recorro cada una de las columnas que se generan en dentrites
for index, col in enumerate(col_dentrites):
    
    
    with col:
        
        # Estas variables primeras almacenan numeros para las key de las casillas de datos
        # y para mostrar en que peso se esta trabajando
        titles = index 
        key_name_peso = "p" + str(index)
        
        peso_title = st.markdown(f'$w_{titles}$')
        peso = st.number_input('Introduce un valor', 0.0, 100.0, key=key_name_peso)
        # Aqui agrego a la lista w el valor de peso
        w.append(peso)
        
st.markdown(f'$w$ = {w}')
          
st.markdown('### Entradas')

# Columnas donde se generan los imputs
col_dentrites_2 = st.columns(dentrites)

for index, col in enumerate(col_dentrites_2):
        
    with col:
        
        # Estas variables primeras almacenan numeros para las key de las casillas de datos
        # para que sean diferentes y para mostrar en que inputs se esta trabajando.
        titles = index
        key_name_value = "v" + str(index)
        
        input_value_title = st.markdown(f'$x_{titles}$')
        input_value = st.number_input('Introduce un valor', key=key_name_value)
        # Aqui agrego a la lista x el valor de input value.
        x.append(input_value)
    
st.markdown(f'$x$ = {x}')

# Aqui genero las columnas para el sesgo y la selección de función de activación    
col1, col2 = st.columns(2)
    
with col1: 
    st.markdown('### Sesgo')
    # Aqui almaceno el valor para el sesgo
    sesgo = st.number_input('Introduce un valor', key='bias_0')
    
with col2: 
    st.markdown('### Función de activación')
    # Aquí almaceno la función de activación seleccionada
    activation_function = st.selectbox('Elige la función de activación', ['Sigmoide', 'ReLU', 'Tangente hiperbólica'])
    
    
if st.button('Calcular la salida :zap:'):
    # Instanciación de la clase Neuron
    neuron = Neuron(w, sesgo, activation_function)
    # Llamo al metodo run de la clase neuron para que realice los calculos correspondientes.
    output = neuron.run(x)
    # Saco por pantalla el resultado del metodo run
    st.markdown(f'### La salida de la neurona es :green[{output}]')
