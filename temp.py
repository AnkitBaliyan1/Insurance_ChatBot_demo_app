
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
        st.write("database app now")
        #data_base_model.database_app()
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