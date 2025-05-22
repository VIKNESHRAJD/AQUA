import streamlit as st

st.title("🎓 CGPA Calculator")

st.write("Enter your grades for each subject to calculate your CGPA.")

# Input number of subjects
num_subjects = st.number_input("Enter number of subjects", min_value=1, step=1)

grades = []

for i in range(num_subjects):
    grade = st.number_input(f"Enter CGPA for Subject {i + 1}", min_value=0.0, max_value=10.0, step=0.01)
    grades.append(grade)

if st.button("Calculate CGPA"):
    if len(grades) > 0:
        cgpa = sum(grades) / len(grades)
        st.success(f"🎉 Your CGPA is: {cgpa:.2f}")
    else:
        st.warning("Please enter valid grades.")
