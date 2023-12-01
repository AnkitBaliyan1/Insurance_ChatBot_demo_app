import streamlit as st
from streamlit_option_menu import option_menu
import about, user_file_model

st.title("launching app")

# Dummy user data
users = {
    "admin": "password123",
    "user1": "mypassword"
}

# Define functions for each page
def info_page():
    st.title('Info')
    st.write('This is the info page.')

def contact_page():
    st.title('Contact Us')
    st.write('This is the contact us page.')

# Function to verify credentials
def check_credentials(username, password):
    return username in users and users[username] == password

# Function to handle logout
def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''

# Login Page
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
        else:
            st.error("Incorrect username or password")


def main():
    st.title("running app")
