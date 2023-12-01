import streamlit as st
from streamlit_option_menu import option_menu
import about, user_file_model, data_base_model

st.title("ClaimComrade Web App")

# Dummy user data
users = {
    "admin": "password123",
    "user1": "mypassword",
    "kunal": "weEkpassword"
}

# Define functions for each page
def info_page():
    st.title('Info')
    st.write('No information here.')

def contact_page():
    st.title('Contact Us')
    st.subheader('For technical assistance: 9958631596')
    st.subheader("For domain assistance: xxxxxxxxxxx")
    footer_style = """
            <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f1f1f1;
                color: black;
                text-align: center;
                padding: 10px;
                font-size: 16px;
            }
            </style>
        """

    # Add custom CSS for the footer
    st.markdown(footer_style, unsafe_allow_html=True)

    # Adding the footer
    footer = """
        <div class="footer">
        <p><strong>Note:</strong> We're here to help you from 10 AM to 6 PM!</p>
        </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

    st.markdown(""" 
                **Note:** We're here to help you from 10 AM to 11 AM!
                """, unsafe_allow_html=True)

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





