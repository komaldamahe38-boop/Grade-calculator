import streamlit as st


st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #dbeafe, #bfdbfe);
}

h1 {
    color: #1e3a8a;
    text-align: center;
}

label {
    color: #1e40af !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
# Title
st.title("🎓 Grade Calculator")
#institude name
Is_name=st.text_input("Enter institude Name")

# Student Name
name = st.text_input("Enter Student Name")

# Marks Input
m1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100)
m2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100)
m3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100)
m4 = st.number_input("Subject 4 Marks", min_value=0, max_value=100)
m5 = st.number_input("Subject 5 Marks", min_value=0, max_value=100)

# Button
if st.button("Calculate Result"):

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    # Grade Logic
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Display Result
    st.subheader("Result")
    st.write("Institude name :", Is_name)
    st.write("Student Name:", name)
    st.write("Total Marks:", total, "/ 500")
    st.write("Percentage:", round(percentage, 2), "%")
    st.success(f"Grade: {grade}")