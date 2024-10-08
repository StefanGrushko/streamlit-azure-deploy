import streamlit as st

# Title of the app
st.title("Streamlit App Deployed to Azure App Service")

# Input text
name = st.text_input("Enter your name:")

# Button to submit
if st.button("Submit"):
    # If name is entered, display a greeting
    if name:
        st.write(f"Hello, {name}!")
    else:
        st.write("Please enter a name.")
