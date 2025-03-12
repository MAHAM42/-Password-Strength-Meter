import streamlit as st
import re
import random
import string

def check_password_strength(password):
    strength = "Weak"
    color = "red"
    suggestions = []
    
    length_criteria = len(password) >= 12
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    number_criteria = bool(re.search(r"[0-9]", password))
    special_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    score = sum([length_criteria, uppercase_criteria, number_criteria, special_criteria])
    
    if not length_criteria:
        suggestions.append("Use at least 12 characters.")
    if not uppercase_criteria:
        suggestions.append("Include at least one uppercase letter.")
    if not number_criteria:
        suggestions.append("Add at least one number.")
    if not special_criteria:
        suggestions.append("Use at least one special character.")
    
    if score == 4:
        strength = "Strong"
        color = "green"
    elif score == 3:
        strength = "Medium"
        color = "orange"
    
    return strength, color, suggestions

def generate_strong_password(length=14, include_upper=True, include_numbers=True, include_special=True):
    characters = string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += "!@#$%^&*()"
    
    return ''.join(random.choice(characters) for _ in range(length))

# Header
st.markdown("""
    <div style='background: linear-gradient(90deg, #ff9a9e, #fad0c4, #fad0c4, #ffdde1); padding: 20px; border-radius: 10px;'>
        <h1 style='text-align: center; color: #4A148C;'>🔒 Password Strength Meter</h1>
        <p style='text-align: center; color: #1A237E;'>Ensure your password is strong and secure!</p>
    </div>
    <hr>
""", unsafe_allow_html=True)

# Password Input
st.markdown("""
    <style>
        input[type="password"] {
            background: linear-gradient(90deg, #ff9a9e, #fad0c4, #ffdde1);
            border-radius: 5px;
            padding: 10px;
            border: none;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)
password = st.text_input("Enter Password", type="password")

def handle_check_password():
    if password:
        strength, color, suggestions = check_password_strength(password)
        st.markdown(f"<h3 style='color:{color};'>Strength: {strength}</h3>", unsafe_allow_html=True)
        if suggestions:
            st.warning("⚠️ Suggestions to improve:")
            for suggestion in suggestions:
                st.write(f"- {suggestion}")
        if st.button("Try Again"):
            st.experimental_rerun()

if password and st.button("Check Password Strength"):
    handle_check_password()

# Password Generator
st.markdown("""
    <style>
        div.stButton > button {
            background: linear-gradient(90deg, #ff9a9e, #fad0c4, #ffdde1);
            color: #4A148C;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }
        div.stButton > button:hover {
            background: linear-gradient(90deg, #ff758c, #ff7eb3);
        }
    </style>
""", unsafe_allow_html=True)

if st.button("Generate Strong Password"):
    length = len(password) if password else 14
    include_upper = bool(re.search(r"[A-Z]", password)) if password else True
    include_numbers = bool(re.search(r"[0-9]", password)) if password else True
    include_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)) if password else True
    
    new_password = generate_strong_password(length, include_upper, include_numbers, include_special)
    st.success(f"🔑 Suggested Password: {new_password}")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: #6A1B9A;'>Made with ❤️ Maham Shahid</p>
""", unsafe_allow_html=True)
