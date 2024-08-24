import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title('My Streamlit Dashboard')

# Sidebar
option = st.sidebar.selectbox('Select a number:', [1, 2, 3, 4])

# Display data
st.write(f'You selected: {option}')

# Example data
data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randn(10)
})

# Display chart
st.line_chart(data)
