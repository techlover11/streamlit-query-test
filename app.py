import streamlit as st
import pandas as pd
from streamlit_condition_tree import condition_tree, config_from_dataframe

st.title("Streamlit Condition Tree Example")

# Initial dataframe
df = pd.DataFrame({
    'First Name': ['Georges', 'Alfred', 'Dieter'],
    'Age': [45, 98, 17],
    'Favorite Color': ['Green', 'Red', 'Yellow'],
    'Like Tomatoes': [True, False, True]
})

st.write("Initial DataFrame:")
st.write(df)

# Basic field configuration from dataframe
try:
    config = config_from_dataframe(df)
    st.write("Config:")
    st.write(config)
except Exception as e:
    st.error(f"Error in config_from_dataframe: {e}")

# Condition tree with error handling
try:
    query_string = condition_tree(config)
    st.write("Query String:")
    st.write(query_string)
except Exception as e:
    st.error(f"Error generating query string: {e}")

# Filtered dataframe
if 'query_string' in locals() and query_string:
    try:
        df_filtered = df.query(query_string)
        st.write("Filtered DataFrame:")
        st.write(df_filtered)
    except Exception as e:
        st.error(f"Error filtering dataframe: {e}")
else:
    st.write("No query string generated. Please define conditions using the condition tree.")
