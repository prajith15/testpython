import streamlit as st

# Hardcoded credentials (for demo purpose only)
USERNAME = "admin"
PASSWORD = "1234"

# Set the title
st.title("🔐 Simple Login Page")

# Input fields
username = st.text_input("Username")
password = st.text_input("Password", type="password")
st.button("Login")
# Login button
if username == USERNAME and password == PASSWORD:
    st.success(f"✅ Logged in successfully! Welcome, {username} 🎉")
else:
    st.error("❌ Invalid username or password")
