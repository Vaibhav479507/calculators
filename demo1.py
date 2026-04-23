import streamlit as st

# Title
st.title('Calculator App')

# Input
num1 = st.number_input('Enter first number')
num2 = st.number_input('Enter second number')

# Operaation selection
operation = st.selectbox(
    'Choose operation',
    ['Addition', 'Subtraction','Multiplication','Division']
)

# Function
def calculate(a, b, op):
    if op == 'Addition':
        return a + b
    elif op == 'Subtraction':
        return a - b
    elif op == 'Multiplication':
        return a * b
    elif op == 'Division':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
        

# Button
if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")        
    