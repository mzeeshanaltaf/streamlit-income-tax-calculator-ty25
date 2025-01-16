import streamlit as st
from tax import *

# Configure the settings of the webpage
st.set_page_config(page_title="Income Tax Calculator", page_icon="🧊", layout="centered")

st.title('Income Tax Calculator for TY 2025')
st.write('Income Tax Calculator for Pakistani Salaried Individuals for Tax Year 2025.')
st.write('Enter your monthly salary '
         'and it will calculate your tax liability for tax year 2024 and 2025. It will also display the net annual '
         'change in tax liability.')

st.subheader('Enter Monthly Salary in PKR')
monthly_salary = st.number_input('Enter Monthly Salary', min_value=0.0, value=50_000.0, format='%f', step=10_000.0,
                                 placeholder='Enter Monthly Salary in PKR', label_visibility='collapsed')
annual_salary = monthly_salary * 12
it_ty_25 = tax_calculation_ty25(annual_salary)
it_ty_24 = tax_calculation_ty24(annual_salary)

it_24_percent = (it_ty_24/annual_salary) * 100
it_25_percent = (it_ty_25/annual_salary) * 100

net = format_number((it_ty_25 - it_ty_24))
if net == 0:
    perc_change = 0
else:
    perc_change = round((net/it_ty_24) * 100, 2)

col1, col2, col3 = st.columns(3)
col1.metric("Annual Tax TY24", f"{it_ty_24:,}", delta=f"{it_24_percent:.2f}")
col2.metric("Annual Tax TY25", f"{it_ty_25:,}", delta=f"{it_25_percent:.2f}")
col3.metric(":blue[Net Annual Change]", f"{net:,}", delta=f"{perc_change}%", delta_color='inverse')

st.subheader('Contact')
with st.expander('Queries/Questions:'):
    st.markdown(''' Any queries/questions: Contact [Zeeshan Altaf](mailto:zeeshan.altaf@gmail.com)''')
