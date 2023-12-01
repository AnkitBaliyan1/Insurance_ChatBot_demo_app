import streamlit as st

def main():

    st.title("About Us")


    st.write("We are a small team working towards cracking the insurance industry complex concept and terms for common user.")

    st.write("Our products:")

    st.subheader("1. InsureBuddy")

    st.write("Ask me anything from my databasae")

    trained_files = ['9.3 INSURANCE LAW AND PRACTICE_CS.pdf',
        'Guidebook on Health Insurance.pdf',
        'Insurance_Basics information ebook.pdf',
        'Principles of Insurance_LOMA.pdf',
        'ic 14 regulation of ins business for Licentiate Exam of III.pdf',
        'Health Insurance: Are We Covered? - Sorin Investments.pdf',
        'Q&A_ insurance & reinsurance regulation in India - Lexology.pdf']
    
    
    st.write("Files the model is trained for: ")
    for i, file in enumerate(trained_files):
        st.write(f"{i+1}. {file}")

    st.subheader("2. DocQueryWizard")

    st.write("Upload your file and ask me anything out of it")
    