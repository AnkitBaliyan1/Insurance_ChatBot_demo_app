import streamlit as st
#import os
from openai._client import OpenAI
import time
from datetime import datetime
import pandas as pd
import os


API_KEY = st.secrets['OPENAI_API']


def update_log_file(user, question, answer):
    file_path = "/logbook/logbook.csv"
    # Read existing data or create a new DataFrame if file doesn't exist
    try:
        df = pd.read_csv(os.path.join(file_path,'logbook.csv'))
        st.write("file read successfully")
    except FileNotFoundError:
        df = pd.DataFrame(columns=['user', 'time', 'question', 'answer'])

    # Add new entry
    new_entry_df = pd.DataFrame({
        'user': [user],
        'time': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        'question': [question],
        'answer': [answer]
    })

    # Concatenate the new entry with the existing DataFrame
    df = pd.concat([df, new_entry_df], ignore_index=True)

    # Save updated data
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False)
    except PermissionError as e:
        # Handle the error, e.g., log it, use an alternative path, or notify the user
        #st.write("Permission denied: Unable to create directory.")
        pass

    #df.to_csv("logbook.csv", index=False)
    st.write(df)




def database_app():
    client = OpenAI(api_key = API_KEY)

    # these files are already given to the assistent, with following file_id
    file_ids = ['file-GE91jMYXkQ2QiVVrcwz6G7wh',
        'file-cJsfuNfu18AOP9dN3asYrxfS',
        'file-Gm44wTSYk5mHRmhwuH4t6pgb',
        'file-OKGamfHqaNEzivBw0absVaBR',
        'file-sx4ChdDMpItOEgKBsGC9AEkL',
        'file-ZwFicx7NU8AUGNBgNCUomxQj',
        'file-ufqJN5sFWNVj2nAmpWtXNkXf']

    assistant_id = 'asst_gja1V67PclQreusUebPq7Sq1'

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
                    final_answer = i.content[0].text.value
                    st.write(final_answer)
                    if i.role == 'assistant':
                        update_log_file(user=st.session_state['username'], question=user_prompt, answer=final_answer)
                        



