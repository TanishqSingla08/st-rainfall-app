import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    data = pd.read_csv('FinalData.csv')
    return data

def main():
    data = load_data()

    if st.checkbox('Show Dataframe'):
        st.dataframe(data)

    state = st.selectbox('Select a State/UT:', data['States.UTs'].unique())
    year = st.slider('Select a Year:', min_value=1900, max_value=2017)
    
    col1, col2 = st.columns(2)
    with col1:
        op1 = st.button("Monthly")
    with col2:
        op2 = st.button("Quarterly")

    if op1:
        months = pd.DataFrame(data.iloc[:, 2:14])
        filtered_data = months[(data['States.UTs']==state) & (data['YEAR']==year)]
        st.dataframe(filtered_data)

        plt.bar(months.columns, filtered_data.values[0])
        plt.xlabel('Months')
        plt.ylabel('Rainfall (in mm)')
        plt.title('Histogram of Rainfall by Month')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    elif op2:
        quarter = pd.DataFrame(data.iloc[:, 14:18])
        filtered_data = quarter[(data['States.UTs']==state) & (data['YEAR']==year)]
        st.dataframe(filtered_data)

        plt.bar(quarter.columns, filtered_data.values[0])
        plt.xlabel('Quarters')
        plt.ylabel('Rainfall (in mm)')
        plt.title('Histogram of Rainfall by Quarter')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

if __name__ == '__main__':
    main()