import streamlit as st
import plotly.express as px
from numpy import random
import numpy as np
import pandas as pd
from PIL import Image
df = pd.read_csv("C:/Users/DHEERAJ/OneDrive/Desktop/sih/Hackathon/finalfinal.csv")

st.set_page_config(
    page_title='Real time dashboard',
    page_icon='🌟',
    layout='wide'
)
# TOP KPI's
total_patients =500
discharged_count = df.loc[df['Status_Info'] == 'Discharged'].count()[0]
died_count = df.loc[df['Status_Info'] == 'Died'].count()[0]


# Calculate the percentage of positive reviews
yes_count = df['Positive_Review'].value_counts().get('Yes', 0)
total_reviews = df['Positive_Review'].count()  # Total count of reviews
positive_percentage = (yes_count / total_reviews) * 100  # Calculate percentage

# Calculating emergency Cases
Emergency_count = df.loc[df['Type_Of_Admission'] == 'Emergency'].count()[0]


st.markdown("<h1 style='margin-top: -10px;'>Dashboard 📊</h1>", unsafe_allow_html=True)

 
st.markdown("<hr style='border: 2px solid #ccc;'>", unsafe_allow_html=True)
st.subheader('Metrics')
st.markdown("<hr style='border: 0.5px solid #ccc;'>", unsafe_allow_html=True)
# Create columns for layout

col1, col2, col3 = st.columns(3)
with col1:
 st.metric(label="Discharged 🛏️", value=discharged_count, delta=10, delta_color="normal")
 st.metric(label="No Of Patients Died ❌", value=died_count, delta=2, delta_color="inverse")
  
with col2:
    st.metric(label="Positve Reviews ✅", value=f"{positive_percentage:.2f}%", delta=1.5, delta_color="normal")
    st.metric(label="Revenue 💵", value=15324, delta=5000, delta_color="normal")

with col3:
    st.metric(label="Avg Waiting Time ⌛", value=20, delta=-5.6, delta_color="normal")
    st.metric(label="Emergency Cases ⚠️", value= Emergency_count, delta=-8, delta_color="inverse")

st.markdown("<hr style='border: 2px solid #ccc;'>", unsafe_allow_html=True)
disease_filter = st.selectbox("select the disease", df["D_name"].unique())
placeholder = st.empty()

if (disease_filter == 'Diabetes'):
    filtered_df = df.query("D_name == 'Diabetes'")
elif (disease_filter == 'cardio arrest'):
    filtered_df = df.query("D_name == 'cardio arrest'")
elif (disease_filter == 'respiratory problems'):
    filtered_df = df.query("D_name == 'respiratory problems'")
elif (disease_filter == 'Covid'):
    filtered_df = df.query("D_name == 'Covid'")
elif (disease_filter == 'Hypertension'):
    filtered_df = df.query("D_name == 'Hypertension'")
elif (disease_filter == 'TB'):
    filtered_df = df.query("D_name == 'TB'")
elif (disease_filter == 'Cancer'):
    filtered_df = df.query("D_name == 'Cancer'")
elif (disease_filter == 'Infant_and_Pregnancy cases'):
    filtered_df = df.query("D_name == 'Infant_and_Pregnancy cases'")
elif (disease_filter == 'accident_cases'):
    filtered_df = df.query("D_name == 'accident_cases'")
else:
    filtered_df = df  # Handle the default case here

fig1, fig2,fig3= st.columns(3) 
with fig1:
    if filtered_df is not None:
        st.subheader('{}'.format(disease_filter))
        gender_counts = filtered_df['Gender'].value_counts()
        st.bar_chart(gender_counts)

with fig2:
    if filtered_df is not None:
        st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
        location_gender = pd.crosstab(filtered_df["Location"], df['Gender'])
        st.bar_chart(location_gender)
with fig3:
     if filtered_df is not None:
#         st.subheader('Disease Distribution by Gender')
         st.markdown("<div style='height: 70px;'></div>", unsafe_allow_html=True)
         local_disease = pd.crosstab(filtered_df['Location'], filtered_df['D_name'])
         st.area_chart(local_disease) 
st.markdown("<hr style='border: 2px solid #ccc;'>", unsafe_allow_html=True)
figu1 , figu2 = st.columns(2)
with figu1:
    status_info_counts = filtered_df['Status_Info'].value_counts()
    fig_status_info_pie = px.pie(values=status_info_counts, names=status_info_counts.index)
    st.subheader('Status Info Distribution')
    st.plotly_chart(fig_status_info_pie)
    

with figu2:
    blood_gender = pd.crosstab(filtered_df['Blood_Type'], filtered_df['Gender'])
    fig_blood_gender = px.bar(blood_gender, barmode='group')
    st.subheader('Blood Type Distribution by Gender')
    st.plotly_chart(fig_blood_gender)   
    



  
st.markdown("<hr style='border: 3px solid #ccc;'>", unsafe_allow_html=True)
# Selectbox to select visualization
visualization_option = st.selectbox('Select Visualization', ('Disease Distribution by Gender',
                 'Blood Distribution By Gender', 'Location Count',
                   'Addiction Count',
                   'Addiction vs. Gender',
                   'Status Info Distribution Pie','Status Info Counts',
                 'Type of Admission Counts'))

if visualization_option == 'Disease Distribution by Gender':
     st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
     st.subheader('Disease Distribution by Gender')
     st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
     disease_gender = pd.crosstab(df['D_name'], df['Gender'])
     st.bar_chart(disease_gender)

elif visualization_option == 'Blood Distribution By Gender':
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.subheader('Blood Distribution By Gender')
    blood_gender = pd.crosstab(df['Blood_Type'], df['Gender'])
    st.bar_chart(blood_gender)

elif visualization_option == 'Location Count':
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.subheader('Count of patients by location')
    st.bar_chart(df['Location'].value_counts())

elif visualization_option == 'Addiction Count':
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.subheader('Count of patients by addiction status')
    st.bar_chart(df['Addiction'].value_counts())

elif visualization_option == 'Diseases distribution age wise': 
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.subheader('Age distribution in each disease (Stacked Bar Chart)')
    stacked_bar_chart = grouped.plot(kind='bar', stacked=True, figsize=(6, 5))
    st.pyplot()

elif visualization_option == 'Addiction vs. Gender':
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.subheader('Addiction Distribution by Gender')
    # Creating a cross-tab for addiction vs gender and visualizing it
    addiction_gender = pd.crosstab(df['Addiction'], df['Gender'])
    st.bar_chart(addiction_gender)
elif visualization_option == 'Status Info Distribution Pie':
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.subheader('Status Info Distribution')
    status_info_counts = df['Status_Info'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(status_info_counts, labels=status_info_counts.index, autopct='%1.1f%%')
    st.pyplot(fig)
elif visualization_option == 'Status Info Counts':
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.subheader('Status Info Counts')
    status_info_counts = df['Status_Info'].value_counts()
    st.bar_chart(status_info_counts)

elif visualization_option == 'Type of Admission Counts':
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
    st.subheader('Type of Admission Counts')
    type_of_admission_counts = df['Type_Of_Admission'].value_counts()
    st.bar_chart(type_of_admission_counts)
st.markdown("<hr style='border: 2px solid #ccc;'>", unsafe_allow_html=True)

