import streamlit as st
#import os
from openai._client import OpenAI
import time
import pandas as pd
import os

API_KEY = st.secrets['OPENAI_API']


def database_app():
    client = OpenAI(api_key = API_KEY)

    trained_files = ['9.3 INSURANCE LAW AND PRACTICE_CS.pdf',
        'Guidebook on Health Insurance.pdf',
        'Insurance_Basics information ebook.pdf',
        'Principles of Insurance_LOMA.pdf',
        'ic 14 regulation of ins business for Licentiate Exam of III.pdf',
        'Health Insurance: Are We Covered? - Sorin Investments.pdf',
        'Q&A_ insurance & reinsurance regulation in India - Lexology.pdf']
    
    with st.container():
        st.write("Files the model is trained for: ")
        for i, file in enumerate(trained_files):
            st.write(f"{i+1}. {file}")

    # these files are already given to the assistent, with following file_id
    file_ids = ['file-hDhdvqkJChYdkzttGFZ6S28b',
    'file-7D9IReBqreOlI2nmAa89KXvy',
    'file-NgBpE07Ve7WcdOJoVHNvI0rl',
    'file-NYABDUzSMSrgBDyd8TYoCspj',
    'file-rurOHDUhqHTq8LvL3geWlUKb',
    'file-q4jVdVJfLvuYhIwnS5tS9mzE',
    'file-KMYHVuEHwdd2NxiUsI6sUVlN']

    assistant_id = 'asst_LMC3TpkbxsFtbVPcPH3UGoec'

    # creating thread 
    thread = client.beta.threads.create()


    # user question
    user_prompt = st.text_input("How can I help you?")
    #"what is the Special Conditions and Exclusions in this policy? The response should be in simple language."


    if st.button("Generate Response"):
        if not user_prompt:
            st.error("Please enter your question above.")
        else:
            with st.spinner():
                # prompting user question to the assistant
                ## note: here that the user prompt is added to the thread.
                message = client.beta.threads.messages.create(
                    thread_id=thread.id,
                    role="user",
                    content= user_prompt
                )

                # runs to converge thread id and assistant id
                run = client.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant_id,
                instructions="Response should end with I hope you liked the response. Let's try another one."
                )

                to_run=True
                while to_run:
                    # converge run id and thread id to overlap with assistant.
                    run = client.beta.threads.runs.retrieve(
                    thread_id=thread.id,
                    run_id=run.id
                    )
                    time.sleep(1)
                    if run.status == 'completed':
                        to_run=False

                # reterive messages from from assistant
                messages = client.beta.threads.messages.list(
                thread_id=thread.id
                )

                # creating it to view the response and prompt
                for i in reversed(messages.data):
                    st.write(i.role + " :")
                    st.write(i.content[0].text.value)


