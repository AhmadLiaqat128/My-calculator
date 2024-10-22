import streamlit as st

# Title of the calculator
st.title("Simple Calculator")

# Input fields for numbers
number1 = st.number_input("Enter first number", value=0.0)
number2 = st.number_input("Enter second number", value=0.0)

# Dropdown for selecting an operation
operation = st.selectbox("Choose operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Function to perform calculation based on the selected operation
def calculate(num1, num2, op):
    if op == "Addition":
        return num1 + num2
    elif op == "Subtraction":
        return num1 - num2
    elif op == "Multiplication":
        return num1 * num2
    elif op == "Division":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Button to perform the calculation
if st.button("Calculate"):
    result = calculate(number1, number2, operation)
    st.write(f"The result of {operation} is: {result}")
