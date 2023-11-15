import streamlit as st

def organizationProfiler():
    profileName = st.text_input("Enter the Organization Name")
    profileAlias = st.text_area("Enter Aliases")
    profileGender = st.radio("Select the Gender", ("Male", "Female", "Other"))
    profileAge = st.text_input("Enter No. of Years")
    profileDOB = st.text_input("Enter DOB")
    profilePrimeLocation = st.text_input("Enter Primary Location")
    profileOtherLocations = st.text_area("Enter Other Associated Locations")
    profileCountry = st.text_area("Enter Country")
    profilePincode = st.text_area("Enter Pincode")
    profileFamilyBack = st.text_area("Family Background Details")
    profileRelatedURL = st.text_area("Enter Associated URLs - separated with ','")
    profileSIN = st.text_input("Social Identity Number")
    profileBank = st.text_area("Enter Banking Details")
    profileState = st.text_input("Enter Region/State/Province")
    profileRegional = st.text_area("Enter District/Town/Village")
    profileOtherDetails = st.text_area("Enter Other Details")
    profileCriminalHistory = st.text_area("Enter Criminal History")
    profileIdentificationMarks = st.text_area("Enter Identification Marks")
    profilePrimaryLanguage = st.text_input("Enter Primary Language")
    profileSecondaryLanguage = st.text_input("Enter Secondary Language")
    profileBloodGroup = st.text_input("Enter Blood Group")
    profileAssociations = st.text_input("Enter Associations")
    profileFamilyDetails = st.text_area("Enter Family Details")
    profilePrimaryEmail = st.text_input("Enter Primary Email")
    profileSecondaryEmail = st.text_input("Enter Secondary Email")
    profileOccupation = st.text_input("Enter Current Occupation")
    profilePrevOccupation = st.text_area("Enter Previous Occupations")
    profileDesignation = st.text_input("Enter Current Designation")
    profilePrevDesignation = st.text_area("Enter Previous Designations")
    profileEducationalBG = st.text_area ("Enter Educational Details")
    profileCategory = st.multiselect("Select Category Tags", ["Category1", "Category2", "Category3"])
    profileThreat = st.slider("Threat Level", 0, 10)
    profileDescription = st.text_area("Please Enter Description")
    with st.expander("Select Social Media Sources"):
        socialTwitter = st.text_input("Enter Twitter Handle")
        socialFacebook = st.text_input("Enter Facebook URL")
        socialRelatedFBPages = st.text_area("Enter Facebook Groups & Pages URLs")
        # Add other social media inputs here
        
    profileUploadContainer = st.file_uploader("Upload Related Documents", accept_multiple_files=True)
    for fileUpload in profileUploadContainer:
        bytesData = fileUpload.read()
        st.write("FileName:", fileUpload.name)
        st.write(bytesData)
            
    


def organizationDatasource():
    selectedDatasource = st.selectbox('Data Source Type', ['Social Media', 'News Feeds'])
    if selectedDatasource == 'Social Media':
        datasourceType = st.selectbox('Social Media Type', ['Twitter', 'Facebook Group', 'Facebook Page', 'Facebook Account', 'Instagram', 'Wikipedia', 'Reddit', 'WordPress', 'Dailymotion', 'YouTube', 'Weibo', 'Tiktok', 'Telegram'])
    elif selectedDatasource == 'News Feeds':
        st.write("Thank You!")

def main():
    st.title("Forms in Streamlit")
    with st.form(key="completeFeedForm"):
        st.write("Manual Data Feeder")
        countrySelect = st.selectbox('Country', ['Global', 'Australia', 'Bangladesh', 'China', 'Dijbouti', 'Egypt', 'France', 'Germany', 'Hong Kong', 'Indonesia', 'India', 'Italy', 'Israel', 'Iran', 'Iraq', 'Japan', 'Kazakhstan', 'Libya', 'Maurities', 'Malaysia', 'Nigeria', 'Oman', 'Pakistan', 'Qatar', 'Russia', 'SriLanka', 'Singapore', 'Taiwan', 'Turkey', 'United States of America', 'United Kingdom', 'Vietnam', 'Yemen', 'Zimbabwe'])
        if countrySelect:
            categorySelect = st.selectbox('Category (Select "Organization" for Ingestion)', ['Agriculture', 'Art & Architecture', 'Anti-State', 'Business', 'Climate', 'Corporates & Companies', 'Critical Infrastructure', 'Children & Youth', 'Developments', 'Disaster', 'District', 'Energy', 'Empowerment', 'Entertainment', 'Education', 'Food', 'Finance', 'Faultlines', 'Flora Fauna', 'Foreign Affairs & Relations', 'Geo-Politics', 'Government', 'Health, Hospitals & Hygiene', 'Home', 'Industries', 'Information Technology & Security', 'Intelligence', 'Innovation', 'Joint Ventures & Congress', 'Kaleidoscope', 'Law & Enforcement', 'Life', 'Local', 'Market & Retails', 'Military & Defence', 'News', 'Nuclear', 'Nature', 'Network', 'Organizations', 'Office', 'Occult', 'Personnel', 'Property', 'Peace & Prosperity', 'Politics', 'Questions', 'Region', 'Religion & Culture', 'Safety & Security', 'Social', 'Science', 'Terrorism & Threats', 'Traditions', 'Tolerance & Humanity', 'Tourism & Travel', 'Universe & Unity', 'Universities', 'Warfare', 'Weapons & Armaments', 'Wonders', 'Wildlife'])
            st.form_submit_button("Option Select")
            if categorySelect == "Organizations":
                selectedMenuOption = st.selectbox('Select Option', ('Manual Profiler', 'Data Source'))
                if selectedMenuOption == 'Manual Profiler':
                    st.write("Note: Multiple entries should be separated with ',' (Comma) ")
                    organizationProfiler()
                elif selectedMenuOption == 'Data Source':
                    organizationDatasource()
            elif categorySelect == "Personnel":
                st.write("Personnel category selected.")
                # Add your personnel form here
        st.form_submit_button("Generate a Report")
            

if __name__ == '__main__':
    main()