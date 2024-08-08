import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for numbers and operation
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)
operation = st.selectbox("Select Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform calculation
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Error: Division by zero!")
        result = "Undefined"

# Display the result
if st.button("Calculate"):
    st.write(f"The result of the {operation.lower()} is: {result}")
