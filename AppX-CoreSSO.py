import subprocess
import streamlit as streamlit
from deta import Deta
import os

API_KEY = os.environ.get('API_KEY')

# Initialize DETA with your API key
deta = Deta(API_KEY)
auth_db = deta.Base("AppX-Auth")  # User authentication database
users_db = deta.Base("AppX-SSO")  # User registration database

def main():
    streamlit.title("Single Sign-On with DETA")
    streamlit.sidebar.title("Navigation")
    
    navigation = streamlit.sidebar.radio("Go to", ["Login", "Register"])

    if navigation == "Login":
        login_page()
    else:
        register_page()

def login_page():
    streamlit.subheader("Login")
    username = streamlit.text_input("UserID")
    password = streamlit.text_input("Password", type="password")
    login_button = streamlit.button("Login")

    if login_button:
        authorized = authorize_user(username, password)
        if authorized:
            streamlit.success("Login successful!")
            authorized_page(username)
        else:
            streamlit.error("Incorrect username or password. Please try again.")

def authorize_user(username, password):
    all_user_data = auth_db.fetch().items
    for user_data in all_user_data:
        if user_data["key"] == username and user_data.get("password") == password:
            return True
    return False

def authorized_page(username):
    streamlit.title("Authorized Page")
    streamlit.write("Welcome to the authorized page!")
    streamlit.success("Redirecting to the Dashboard ...")
    openStreamlitDashboard(username)

def openStreamlitDashboard(username):
    streamlit.write("Opening Authorized Session ...")
    subprocess.Popen(["streamlit","run","AppX-Dashboard.py","--",f"--user_id={username}"], shell=True)

def register_page():
    streamlit.subheader("Register")
    user_id = streamlit.text_input("User ID")
    username = streamlit.text_input("Username")
    email = streamlit.text_input("Email")
    password = streamlit.text_input("Password", type="password")
    confirm_password = streamlit.text_input("Confirm Password", type="password")
    register_button = streamlit.button("Register")

    if register_button:
        if password == confirm_password:
            user_data = {
                "key": user_id,
                "password": password,
                "username": username,
                "email": email
            }
            auth_db.put(user_data)
            users_db.put(user_data)  # Save user registration data
            streamlit.success("Registration successful! You can now log in.")
        else:
            streamlit.error("Passwords do not match. Please try again.")

if __name__ == "__main__":
    main()
