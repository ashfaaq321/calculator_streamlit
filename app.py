import streamlit as st
# Title and input
st.title("Calculator")
input_exp = st.text_input("Enter a valid calculation:")

# Function to generate nudge
def calculate(input_text):
    return eval(input_text)

if st.button("Calculate"):
    res = calculate(input_exp)
    st.write(f"Result: {res}")