import streamlit as st

# Custom alert for invalid height
def show_alert(message):
    st.markdown(f"<div style='background-color:#ff4d4d; padding:10px; border-radius:5px'><span style='color:white; font-weight:bold;'>❌ {message}</span></div>", unsafe_allow_html=True)

# Title and description
st.title("BMI Calculator")
st.write("**Enter your weight and height to calculate your BMI**.")

# User inputs
weight = st.number_input("**Weight (kg):**", min_value=1.0, step=0.1)
height = st.number_input("**Height (m):**", min_value=0.1, step=0.01)

# Calculate and show BMI
if height > 0:
    bmi = weight / (height ** 2)
    st.write(f"**Your BMI is**: **{bmi:.2f}**")
    if bmi < 18.5:
        st.warning("⚠️ Underweight")
    elif bmi < 24.9:
        st.success("✅ Normal weight")
    elif bmi < 29.9:
        st.warning("⚠️ Overweight")
    else:
        # Custom gray-colored "Obese" message
        st.markdown("<div style='background-color:#808080; padding:10px; border-radius:5px; color:white; font-weight:bold;'>❌ Obese</div>", unsafe_allow_html=True)
else:
    show_alert("Enter a valid height to calculate BMI.")