import streamlit as st
import pandas as pd
import pickle

st.markdown("""
<style>
.stButton button{
    width:100%;
    height:55px;
    font-size:20px;
    border-radius:12px;
}

div[data-testid="stMetricValue"]{
    font-size:40px;
}
</style>
""", unsafe_allow_html=True)

# Page Config
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Performance Predictor")
st.markdown(
    "Enter student details and predict the final percentage."
)

# Load Model
with open("student_performance_model.pkl", "rb") as f:
    model = pickle.load(f)

# Inputs

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=14,
        max_value=19,
        value=16
    )

    student_class = st.selectbox(
        "Class",
        [9, 10, 11, 12]
    )

    study_hours = st.number_input(
        "Study Hours Per Day",
        min_value=0.0,
        max_value=10.0,
        value=3.0
    )

    attendance = st.number_input(
        "Attendance Percentage",
        min_value=0,
        max_value=100,
        value=75
    )

    previous_score = st.number_input(
        "Previous Year Score",
        min_value=0,
        max_value=100,
        value=70
    )

with col2:
    math_score = st.number_input(
        "Math Score",
        min_value=0,
        max_value=100
    )

    science_score = st.number_input(
        "Science Score",
        min_value=0,
        max_value=100
    )

    english_score = st.number_input(
        "English Score",
        min_value=0,
        max_value=100
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    internet = st.selectbox(
        "Internet Access",
        ["No", "Yes"]
    )

    activities = st.selectbox(
        "Extracurricular Activities",
        ["No", "Yes"]
    )

parent_edu = st.selectbox(
    "Parental Education",
    ["High School", "Graduate", "Postgraduate"]
)

# Encoding

education_map = {
    "High School": 0,
    "Graduate": 1,
    "Postgraduate": 2
}

parent_edu_encoded = education_map[parent_edu]

gender_male = 1 if gender == "Male" else 0
internet_yes = 1 if internet == "Yes" else 0
activities_yes = 1 if activities == "Yes" else 0

# Predict Button

if st.button("🚀 Predict Percentage"):

    input_data = pd.DataFrame([[
        age,
        student_class,
        study_hours,
        attendance,
        parent_edu_encoded,
        math_score,
        science_score,
        english_score,
        previous_score,
        gender_male,
        internet_yes,
        activities_yes
    ]], columns=[
        'Age',
        'Class',
        'Study_Hours_Per_Day',
        'Attendance_Percentage',
        'Parental_Education',
        'Math_Score',
        'Science_Score',
        'English_Score',
        'Previous_Year_Score',
        'Gender_Male',
        'Internet_Access_Yes',
        'Extracurricular_Activities_Yes'
    ])

    prediction = model.predict(input_data)[0]

    st.success(
        f"🎯 Predicted Final Percentage: {prediction:.2f}%"
    )