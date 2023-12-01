import streamlit as st
import pandas as pd
import os
from streamlit_option_menu import option_menu
import about, data_base_model, user_file_model

# Dummy user data
users = {
    "admin": "password123",
    "user1": "mypassword"
}

# Define functions for each page
def about_page():
    st.title('About')
    st.write('This is the about page.')

def product_page():
    st.title('Product')
    st.write('This is the product page.')

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

# Main app
def main_app():
    # Display username with icon and smaller font at the top right
    if st.sidebar.button('Logout'):
        logout()

    #st.markdown(f"<h2 style='text-align: right; color: gray;'>{st.session_state['username']}</h2>", unsafe_allow_html=True)


    st.markdown(f"""
        <div style='text-align: right;'>
            <span style='font-size: 16px; margin-right: 10px;'>{st.session_state['username']}</span>
            <a href='javascript:void(0);' onclick='if (confirm("Do you want to logout?")) {{window.streamlitPythonData = {{logout: true}};}}'>
                <img src='https://img.icons8.com/ios-filled/50/000000/user-male-circle.png' style='vertical-align: middle; width: 24px;'>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with st.sidebar:
        selected = option_menu("Main Menu", 
            ["About", "ChatBot", "Build your onw ChatBot","Info", "Contact Us"],
            icons=['house', 'cart', 'cart', 'info', 'envelope'],
            menu_icon="cast", default_index=0)

    if selected == 'About':
        about.main()
    elif selected == 'ChatBot':
        data_base_model.database_app()
    elif selected == "Build your onw ChatBot":
        user_file_model.main()
    elif selected == 'Info':
        info_page()
    elif selected == 'Contact Us':
        contact_page()

# App start
if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    login_page()
else:
    main_app()
