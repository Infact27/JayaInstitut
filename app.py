import streamlit as st
import pandas as pd
import pickle

# Load model & fitur
model = pickle.load(open('model.pkl', 'rb'))
features = pickle.load(open('features.pkl', 'rb'))


st.title("🎓 Prediksi Dropout Siswa")

st.write("Masukkan data siswa:")

# INPUT
Admission_grade = st.number_input("Admission Grade", 0.0, 200.0, 120.0)
Previous_qualification_grade = st.number_input("Previous Qualification Grade", 0.0, 200.0, 120.0)
Curricular_units_1st_sem_grade = st.number_input("1st Semester Grade", 0.0, 20.0, 10.0)
Curricular_units_2nd_sem_grade = st.number_input("2nd Semester Grade", 0.0, 20.0, 10.0)
Curricular_units_1st_sem_approved = st.number_input("1st Semester Approved Units", 0, 20, 5)
Curricular_units_2nd_sem_approved = st.number_input("2nd Semester Approved Units", 0, 20, 5)
Tuition_fees_up_to_date = st.selectbox("Tuition Fees Up To Date", [0,1])
Scholarship_holder = st.selectbox("Scholarship Holder", [0,1])

# PREDIKSI
if st.button("Prediksi"):
    input_data = pd.DataFrame([[
        Admission_grade,
        Previous_qualification_grade,
        Curricular_units_1st_sem_grade,
        Curricular_units_2nd_sem_grade,
        Curricular_units_1st_sem_approved,
        Curricular_units_2nd_sem_approved,
        Tuition_fees_up_to_date,
        Scholarship_holder
    ]], columns=features)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ Siswa berpotensi Dropout")
    else:
        st.success("✅ Siswa tidak berpotensi Dropout")
