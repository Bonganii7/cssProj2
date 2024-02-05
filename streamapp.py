import streamlit as st
import numpy as np 
import pandas as pd
import math
import matplotlib.pyplot as plt 


st.markdown("*Research Article*")
st.title("Determine the Band Gap in Germanium")

st.markdown(''' **1Mthembu**
 *Physics student*

''')


st.header('Abstract')
st.info('''In this experiment, the aim is to investigate band gap of a semiconductor Germanium crystal. The conductivity of a germanium chip is measured as a function temperature, therefore, by observing the graph of natural of conductivity and reciprocal of temperature given in kelvin the band gap of germanium is determined.

From the measurements, the conductivity σ is determined plotted against the reciprocal of temperature T. A linear plot is obtained and from the slope the energy gap of germanium is determined to be E_g = 0.83eV  and compared to the theoretical which is E_g = 0.66eV , the %error found between the two values is -25.76%. This validates the experiment because the percentage error is acceptable. 
''')

st.header('Introduction')
st.markdown(''' When a material has the basic structure of an insulator, but with a much smaller energy gap (2 eV or less), its physical properties (e.g. conductivity) become quite different. These small energy gap materials are semiconductors. At ordinary temperatures, electrons in the highest valence levels of semiconducting materials are able to occupy states in the normally empty conduction band (when solids are formed from a collection of atoms, discrete energy levels are replaced with energy bands). ''')

st.header('Experimental Setup')
st.markdown(''' 
Connect the DC power supply via an ammeter and a 330 Ω resistor to points A and B in order to provide a current through the germanium crystal. See to it that the current and voltage controls on the power source are set to zero and the voltage select control on “lag”. To control the current through the sample, set the voltage control on 0 V and turn the current control to about the center position. The current can now be more accurately controlled by using the voltage control on the power supply. 
''')


st.header('Results ')

file = st.file_uploader("Upload a dataset:", type=['xlsx'])
if file:
        # if worked out, then it one is read and showed on a table
        data = pd.read_excel(file)
        st.dataframe(data.head())
 
        # Put a subtitle
        st.markdown("## Rows")
        
        # It shows the total rows of a dataset
        st.markdown(f"__Rows__: {len(data)}")
 
        # Field to select a column 
        column = st.selectbox("Select the column", data.columns)
 
        # if a column was choose, some statistics about this is showed
        if column:    
            st.markdown(f"__NaN rows__: {data[column].isna().sum()}")
            st.markdown(f"__Mean__: {data[column].mean()}")
            st.markdown(f"__Median__: {data[column].median()}")	
            st.markdown(f"__Mode__: {data[column].mode()[0] }")
 


# Put a subtitle
st.markdown("## Charts")
st.info(''' For the following charts, we only consider the relationships between Conductivity versus Temperature Kelvin and ln versus Temperature Reciprocal ''')
#options
options = ['Scatter', 'Line']
chart = st.radio('Choose a chart', options)

# Hide warnings
st.set_option('deprecation.showPyplotGlobalUse', False)

if chart == 'Scatter':

    x_columns_scatter = ['Temperature Reciprocal', 'Temperature(Kelvin)']
    y_columns_scatter = ['ln', 'Conductivity']
    
    x = st.selectbox("Select the X axis", x_columns_scatter)
    y = st.selectbox("Select the Y axis", y_columns_scatter)
    
    if x and y:
        x_values = data[x].values
        x_values = x_values.reshape(-1, 1)
        plt.scatter(x_values, data[y].values)
        plt.xlabel(x)
        plt.ylabel(y)
        st.pyplot()

        # caption
        if x == 'Temperature(Kelvin)' and y == 'Conductivity':
            st.caption('**Figure 1.** Graph 1: Conductivity versus Temperature Kelvin')
           

    
     
elif chart == 'Line':
    
    x_columns_line = ['Temperature Reciprocal', 'Temperature(Kelvin)']
    y_columns_line = ['ln', 'Conductivity']
    
    x = st.selectbox("Select the X axis", x_columns_line)
    y = st.selectbox("Select the Y axis", y_columns_line)
    
    if x and y:
        plt.plot(data[x].values, data[y].values)
        plt.xlabel(x)
        plt.ylabel(y)
        st.pyplot()

        #caption
        if x == 'Temperature Reciprocal' and y == 'ln':
            st.caption('**Figure 1.** Graph 1: ln versus Temperature Reciprocal')

        
       
        
st.header('Conclusion ')
st.markdown(''' The conductivity of Germanium was measured as a function of temperature and the band gap of Germanium semiconductor (Ge) is experimentally found to be  E_g = 0.83eV and the theoretical value is 0.66eV. The error found, is -25.76%.  ''')
