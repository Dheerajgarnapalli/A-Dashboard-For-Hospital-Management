import streamlit as st
import mysql.connector
from numpy import random
import numpy as np
import pandas as pd

# Establish a connection to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="patient"
)
mycursor = mydb.cursor()


D_name =['Diabetes', 'cardio arrest', 'respiratory problems',
          'Covid','Hypertension', 'TB', 'Cancer', 'Infant_and_Pregnancy cases', 'accident_cases']
Gender= ['Male', 'Female']
Age =  np.arange(0,100)
Blood_Type= ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
Location= ['Rural', 'Urban']
Addiction= ['Smoking', 'Alcoholic', 'Drug-addict', 'None']
Status_Info= ['Discharged', 'Admitted', 'Died', 'ICU']
DOS_Days= [1, 2, 3, 4, 5, 6, 7]
Type_Of_Admission= ['Emergency', 'OP', 'IP']
Positive_Review= ['Yes', 'No']
Wait_Time_Mins= np.arange(0,50)


st.title('Input Page')

# Create the input form components
Id = st.number_input("Enter ID")
selected_d_name = st.selectbox('Select Disease Name', D_name)
selected_gender = st.radio('Select Gender', Gender)
selected_age = st.slider('Select Age', int(min(Age)), int(max(Age)))
selected_blood_type = st.selectbox('Select Blood Type', Blood_Type)
selected_location = st.selectbox('Select Location', Location)
selected_addiction = st.selectbox('Select Addiction', Addiction)
selected_status_info = st.selectbox('Select Status Information', Status_Info)
selected_dos_days = st.selectbox('Select DOS Days', DOS_Days)
selected_type_of_admission = st.selectbox('Select Type of Admission', Type_Of_Admission)
selected_positive_review = st.selectbox('Select Positive Review', Positive_Review)
selected_wait_time_mins = st.slider('Select Wait Time (in minutes)', int(min(Wait_Time_Mins)), int(max(Wait_Time_Mins)))



# Display the selected data
if st.button('Submit'):
   
    # Insert data into MySQL database
    sql = "INSERT INTO input_data VALUES (%s,%s, %s, %s,%s, %s, %s,%s, %s,%s, %s, %s)"
    values =(Id,selected_d_name, selected_gender, selected_age , selected_blood_type,
   selected_location, selected_addiction, selected_status_info,
   selected_dos_days ,selected_type_of_admission, selected_positive_review, selected_wait_time_mins)
    mycursor.execute(sql, values)
    #data STORED
    mydb.commit()
    st.success("Data inserted into MySQL database")

# Display inserted data from MySQL database (for verification)
mycursor.execute("SELECT * FROM input_data")
data = mycursor.fetchall()

st.subheader("Data in MySQL Database:")
for row in data:
    st.write(row)
