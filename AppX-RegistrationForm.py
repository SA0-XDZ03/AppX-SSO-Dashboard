import streamlit as streamlit
from deta import Deta

streamlit.set_page_config(
    page_title="Beyond Beacon xAuthCore",
    page_icon="🛡️",
)

streamlit.write("# Welcome to xAuthCore 👋")
streamlit.info("Administrative Panel: Registration Page")


def genRegistrationDetails():
    email = streamlit.text_input("Enter Email Address")
    name = streamlit.text_input("Enter Full Name")
    username = streamlit.text_input("Enter Username")
    password = streamlit.text_input("Enter Password", type="password")
    confirmPassword = streamlit.text_input("Confirm Password", type="password")
    if password and confirmPassword:
        if password == confirmPassword:
            streamlit.success("Password Matched!")
        else:
            streamlit.error("Password Incorrect - Try Again!")
    contactNumber = streamlit.text_input("Enter Phone Number / Emergency Contact")
    return email, name, username, password, contactNumber


def main():
    accountType = streamlit.radio("Account Type", ("Client","Internal User","Administrator"))

    with streamlit.form("form"):
        if accountType == "Client":
            clientID = streamlit.text_input("Enter Client ID")
    #        values = [email, name, username, password, contactNumber]
            email, name, username, password, contactNumber = genRegistrationDetails()
            submitCredentials = streamlit.form_submit_button("Submit")
            if submitCredentials:
                detaClient = Deta(streamlit.secrets["clientData_key"])
                detaClientDB = detaClient.Base("xAuthCoreAppCDB")
                detaClientDB.put({"accountType": accountType, "clientID":clientID, "email": email, "name":name, "username":username, "password":password, "contactNumber":contactNumber})
                streamlit.write(accountType, clientID, email, name, username, password, contactNumber)
                streamlit.success("Succesfully Written Into The Database")
        
        if accountType == "Internal User":
            userID = streamlit.text_input("Enter UID")
            email, name, username, password, contactNumber = genRegistrationDetails()
            submitCredentials = streamlit.form_submit_button("Submit")
            if submitCredentials:
                detaUser = Deta(streamlit.secrets["userData_key"])
                detaUserDB = detaUser.Base("xAuthCoreAppUDB")
                detaUserDB.put({"accountType": accountType, "userID":userID, "email": email, "name":name, "username":username, "password":password, "contactNumber":contactNumber})
                streamlit.write(accountType, userID, email, name, username, password, contactNumber)
                streamlit.success("Succesfully Written Into The Database")
        
        if accountType == "Administrator":
            adminID = streamlit.text_input("Enter AdminID")
            email, name, username, password, contactNumber = genRegistrationDetails()
            submitCredentials = streamlit.form_submit_button("Submit")
            if submitCredentials:
                detaAdmin = Deta(streamlit.secrets["adminData_key"])
                detaAdminDB = detaAdmin.Base("xAuthCoreAppADB")
                detaAdminDB.put({"accountType": accountType, "adminID":adminID, "email": email, "name":name, "username":username, "password":password, "contactNumber":contactNumber})
                streamlit.write(accountType, adminID, email, name, username, password, contactNumber)
            streamlit.success("Succesfully Written Into The Database")
    
if __name__ == '__main__':
    main()