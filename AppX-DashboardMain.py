import streamlit as streamlit
from streamlit_option_menu import option_menu

streamlit.set_page_config(page_title="Advanced Cyber Strategy & Operations Command - ACSOC")

sidebarUserOption = streamlit.sidebar.selectbox("User-Level", ("Administrator","User","Client"))
# CAN IMPLEMENT UAC OPTIONS HERE
# Example: sidebarUserOption == "Administrator" > Display All Options
streamlit.sidebar.divider()
sidebarMainOption = streamlit.sidebar.selectbox("Objective", ("Intelligence Gathering & Analysis", "Strategic Engagement & Reporting", "Cyber Operations"))

def main():

    if sidebarMainOption == "Intelligence Gathering & Analysis":
        streamlit.title("Intelligence Gathering & Analysis Module")
        intelligenceGatheringModules()

    elif sidebarMainOption == "Strategic Engagement & Reporting":
        streamlit.title("Strategic Engagement & Reporting Module")
        strategicEngagementModules()

    elif sidebarMainOption == "Cyber Operations":
        streamlit.title("Cyber Operations")
        cyberOperationsModules()


def intelligenceGatheringModules():
    selectIntelligenceGatheringModule = option_menu(
    menu_title= None,
    options = ["Strategic Intelligence", "Cyber Threat Intelligence"],
    icons = ["pencil-fill", "bar-chart-fill"],
    orientation = "horizontal"
    )

    if selectIntelligenceGatheringModule == "Strategic Intelligence":
        strategicIntelligenceGatheringModule()
        if sidebarUserOption == "Administrator":
            EntityProfiler()
    
    elif selectIntelligenceGatheringModule == "Cyber Threat Intelligence":
        cyberThreatIntelligenceGatheringModule()
    
def strategicIntelligenceGatheringModule():
    with streamlit.form("Strategic Intelligence Gathering Module", clear_on_submit=True):
        siCountry = streamlit.selectbox('Country',['Global','Australia','Bangladesh','China','Dijbouti','Egypt','France','Germany','Hong Kong','Indonesia','India','Italy','Israel','Iran','Iraq','Japan','Kazakhstan','Libya','Maurities','Malaysia','Nigeria','Oman','Pakistan','Qatar','Russia','Sri Lanka','Singapore','Taiwan','Turkey','United States of America','United Kingdom','Vietnam','Yemen','Zimbabwe'])
        # CAN IMPLEMENT INDIVIDUAL COUNTRY SEARCH & FILTER MECHANISHM
        # Example: if siCountry == 'India' 
        siCategory = streamlit.selectbox('Category',['All', 'Agriculture','Art & Architecture','Anti-State','Business','Climate','Corporates & Companies','Critical Infrastructure','Children & Youth','Developments','Disaster','District','Energy','Enpowerment','Entertainment','Academia & Education','Food','Finance','Faultlines','Flora Fauna','Foreign Affairs & Relations','Geo-Politics','Government','Health, Hospitals & Hygiene','Home','Industries','Information Technology & Security','Intelligence','Innovation','Joint Ventures & Congress','Kalideoscope','Law & Enforcement','Life','Local','Market & Retails','Military & Defence','General News','Nuclear','Nature','Network','Organizations','Office','Occult','Personnel','Property','Peace & Prosperity','Politics','Questions','Region','Religion & Culture','Safety & Security','Social','Science','Terrorism & Threats','Traditions','Tolerance & Humanity','Tourism & Travel','Universe & Unity','Universities','Warfare','Weapons & Armaments','Wonders','Wildlife'])
        # CAN IMPLEMENT INDIVIDUAL CATEGORY SEARCH & FILTER MECHANISM
        # Example: if siCategory == 'General News'
        siEntity = streamlit.selectbox('Search Entity',['General Search','Organizational','Personnel'])
        if siEntity == 'Organizational':
            siEntityOrg = streamlit.checkbox('Cyber Threat Intelligence Module')
            if siEntityOrg == True:
                cyberThreatIntelligenceGatheringModule()
        streamlit.divider()
        siSearchBy = streamlit.selectbox('Search By',['Username Search (Social Media)','Named-Entity Search','Keyword Search','Email Search','Phone Search'])   
        streamlit.divider() 
        siSourcesList = ['Social Media','Search Engines','Archives','Deep/Dark Web','Blogs & Forums','News Sites', 'Special Sites & Search Tools']
        siSourcesAll = streamlit.checkbox("Select All Sources")
        if siSourcesAll:
            siSources = streamlit.multiselect("Sources", siSourcesList, siSourcesList)
        else:
            siSources = streamlit.multiselect("Sources", siSourcesList)
        streamlit.divider()
        searchQuery = streamlit.text_input(label='Enter your Search Query')
        searcher = streamlit.form_submit_button("Search")
    
    saveCase = streamlit.button("Save Case")

def cyberThreatIntelligenceGatheringModule():
    domainNameCTI = streamlit.text_input("Enter Domain Name")

def EntityProfiler():
    #MODULE-SELECTION
    selectedProfilerOption = option_menu(menu_title = None, options = ['Organization Profiler', 'Personnel Profiler'], icons=['search','search'], orientation="horizontal")
    if selectedProfilerOption == "Organization Profiler":
        with streamlit.form("organization_profiler", clear_on_submit=True):
            with streamlit.expander("Organization Profiler"):
                streamlit.write("Organization Profiler")
            organizationReport = streamlit.form_submit_button("Generate Report")
            
    else:
        with streamlit.form("user_profiler", clear_on_submit=True):
            with streamlit.expander("Personnel Profiler"):
                profileName = streamlit.text_input("Enter the Person Name")
                profileAlias = streamlit.text_area("Enter Aliases")
                profileGender = streamlit.radio("Select the Gender", ("Male", "Female", "Other"))
                profileAge = streamlit.text_input("Enter No.of Years")
                profileDOB = streamlit.text_input("Enter DOB")
                profilePrimeLocation = streamlit.text_input("Enter Primary Location")
                profileOtherLocations = streamlit.text_area("Enter Other Associated Locations")
                profileCountry = streamlit.text_area("Enter Country")
                profilePincode = streamlit.text_area("Enter Pincode")
                profileFamilyBack = streamlit.text_area("Family Background Details")
                profileRelatedURL = streamlit.text_area("Enter Associated URLs - separated with ','")
                profileSIN = streamlit.text_input("Social Identity Number")
                profileBank = streamlit.text_area("Enter Banking Details")
                profileState = streamlit.text_input("Enter Region/State/Province")
                profileRegional = streamlit.text_area("Enter District/Town/Village")
                profileOtherDetails = streamlit.text_area("Enter Other Details")
                profileCriminalHistory = streamlit.text_area("Enter Criminal History")
                profileIdentificationMarks = streamlit.text_area("Enter Identification Marks")
                profilePrimaryLanguage = streamlit.text_input("Enter Primary Language")
                profileSecondaryLanguage = streamlit.text_input("Enter Secondary Language")
                profileBloodGroup = streamlit.text_input("Enter Blood Group")
                profileAssociations = streamlit.text_input("Enter Associations")
                profileFamilyDetails = streamlit.text_area("Enter Family Details")
                profilePrimaryEmail = streamlit.text_input("Enter Primary Email")
                profileSecondaryEmail = streamlit.text_input("Enter Secondary Email")
                profileOccupation = streamlit.text_input("Enter Current Occupation")
                profilePrevOccupation = streamlit.text_area("Enter Previous Occupations")
                profileDesignation = streamlit.text_input("Enter Current Designation")
                profilePrevDesignation = streamlit.text_area("Enter Previous Designations")
                profileEducationalBG = streamlit.text_area ("Enter Educational Details")
                profileCategoryList = ['Citizen','Terrorist','Government','Private Employee','Journalist','Engineer','Doctor','Military Personnel','Student']
                profileCategory = streamlit.multiselect("Select Category Tags", profileCategoryList)
                profileThreat = streamlit.slider("Threat Level",0,10)
                profileDescription = streamlit.text_area("Please Enter Description")
            
            with streamlit.expander("Select Social Media Sources"):
                socialTwitter = streamlit.text_input("Enter Twitter Handle")
                socialFacebook = streamlit.text_input("Enter Facebook URL")
                socialRelatedFBPages = streamlit.text_area("Enter Facebook Groups & Pages URLs")
                socialInstagram = streamlit.text_input("Enter Instagram Handle")
                socialYouTube = streamlit.text_input("Enter YouTube Channel")
                socialTelegram = streamlit.text_input("Enter Telegram Account")
                socialTelegramChannel = streamlit.text_area("Enter Telegram Channel URLs")
                socialGitHub = streamlit.text_input("Enter GitHub URL")
                socialGoogleMail = streamlit.text_input("Enter Google Mail Address")
                socialProtonMail = streamlit.text_input("Enter Proton Mail Address")
                socialOtherMail = streamlit.text_area("Enter Other Associated Emails")
                socialWhatsApp = streamlit.text_input("Enter WhatsApp Number")
                socialMobiNumbers = streamlit.text_area("Enter Other Associated Numbers")
                socialDiscord = streamlit.text_input("Enter Discord ID")
                socialSkype = streamlit.text_input("Enter Skype ID")
                socialReddit = streamlit.text_input("Enter Reddit ID")
                socialSlack = streamlit.text_input("Enter Slack ID")
                socialOtherMedia = streamlit.text_area("Enter Other Social Media Details")
            
            profileUploadContainer = streamlit.file_uploader("Upload Related Documents", accept_multiple_files=True)
            for fileUpload in profileUploadContainer:
                bytesData = fileUpload.read()
                streamlit.write("FileName:", fileUpload.name)
                streamlit.write(bytesData)                
                
            profilerReport = streamlit.form_submit_button("Generate Report")
            if profilerReport:
                streamlit.success("Report Generated!")
                streamlit.write([profileName, profileAlias, profileGender, profileAge, profileDOB, profilePrimeLocation, profileOtherLocations, profileCountry, profilePincode, profileFamilyBack, profileRelatedURL, profileSIN, profileBank, profileState, profileRegional, profileOtherDetails, profileCriminalHistory, profileIdentificationMarks, profilePrimaryLanguage, profileSecondaryLanguage, profileBloodGroup, profileAssociations, profileFamilyDetails, profilePrimaryEmail, profileSecondaryEmail, profileOccupation, profilePrevOccupation, profileDesignation, profilePrevDesignation, profileEducationalBG, profileCategory, profileThreat, profileDescription, socialTwitter, socialFacebook, socialRelatedFBPages, socialInstagram, socialYouTube, socialTelegram, socialTelegramChannel, socialGitHub, socialGoogleMail, socialProtonMail, socialOtherMail, socialWhatsApp, socialMobiNumbers, socialDiscord, socialSkype, socialReddit, socialSlack, socialOtherMedia, profileUploadContainer])


# # Function to embed an iframe using HTML
# def embed_iframe(link):
#     iframe_code = f'<iframe src="{link}" width="400" height="150"></iframe>'
#     streamlit.markdown(iframe_code, unsafe_allow_html=True)
#     level_two_options = {"Cars" : ["Honda", "Opel", "Tesla"], "Food" : ["Egg", "Pizza", "Spinach"], "Electronics" : ["Headphones", "Laptop", "Phone"]}

#     first_choice = "Cars"
#     first_choice = streamlit.selectbox("First level options", ["Cars", "Food", "Electronics"])
#     second_choice = streamlit.selectbox("Second level options", level_two_options[first_choice], key=first_choice)

#     streamlit.write("You chose: ", second_choice)

# # Create a column with iframes
# option1_iframe_links = [
#     "https://www.example.com/iframe1",
#     "https://www.example.com/iframe2",
#     "https://www.example.com/iframe3",
#     "https://www.example.com/iframe4",
# ]

# def main():
#     # Radio buttons to switch content
#     if sidebar_option == "Option 1":
#         st.title("Option 1 Content")
#         st.write("This is the content for Option 1.")
        
#         cols = st.columns(len(option1_iframe_links))
#         for link, col in zip(option1_iframe_links, cols):
#             with col:
#                 embed_iframe(link)

#     elif sidebar_option == "Option 2":
#         st.title("Option 2 Content")
#         st.write("This is the content for Option 2.")
#     elif sidebar_option == "Option 3":
#         level_two_options = {"Cars" : ["Honda", "Opel", "Tesla"], "Food" : ["Egg", "Pizza", "Spinach"], "Electronics" : ["Headphones", "Laptop", "Phone"]}

#         first_choice = "Cars"
#         first_choice = st.selectbox("First level options", ["Cars", "Food", "Electronics"])
#         second_choice = st.selectbox("Second level options", level_two_options[first_choice])

#         st.write("You chose: ", second_choice)
#         st.title("Option 3 Content")
#         st.write("This is the content for Option 3.")


# import streamlit as st

# # Create a session state to store the page state
# if 'page_state' not in st.session_state:
#     st.session_state.page_state = 'main'

# st.title("Page Content Switching Example")

# if st.session_state.page_state == 'main':
#     st.header("Main Page")
    
#     # Add your main page content here
    
#     if st.button("Go to Page 2"):
#         st.session_state.page_state = 'page2'

# elif st.session_state.page_state == 'page2':
#     st.header("Page 2")
    
#     # Add your content for Page 2 here
    
#     if st.button("Back to Main Page"):
#         st.session_state.page_state = 'main'




# Run the Streamlit app
if __name__ == '__main__':
    main()