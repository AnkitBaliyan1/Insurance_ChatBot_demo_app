import streamlit as st


# Function to validate login
def validate_login(username, password):
    user_credentials = st.secrets["users"].get(username)
    if user_credentials and user_credentials["password"] == password:
        return True
    return False

def main():
    st.subheader("Comming Soon...!")

    # Login form
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if validate_login(username, password):
            st.success("Login successful!")
            # Perform actions for logged-in user
        else:
            st.error("Login failed. Check your username and password.")
