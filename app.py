import streamlit as st
import pandas as pd
from streamlit_condition_tree import condition_tree, config_from_dataframe

st.title("Streamlit Condition Tree Example")

# Initial dataframe
df = pd.DataFrame({
    'First Name': ['Georges', 'Alfred'],
    'Age': [45, 98],
    'Favorite Color': ['Green', 'Red'],
    'Like Tomatoes': [True, False]
})

st.write("Initial DataFrame:")
st.write(df)

# Basic field configuration from dataframe
config = config_from_dataframe(df)

# Condition tree
query_string = condition_tree(config)

st.write("Query String:")
st.write(query_string)

# Filtered dataframe
if query_string:
    df_filtered = df.query(query_string)
    st.write("Filtered DataFrame:")
    st.write(df_filtered)
else:
    st.write("No query string generated. Please define conditions using the condition tree.")
