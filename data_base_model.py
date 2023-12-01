import streamlit as st
#import os
from openai._client import OpenAI
import time
import pandas as pd

API_KEY = st.secrets['OPENAI_API']

current_log_book = pd.DataFrame(columns=['user','time','question','answer'])
#log_book_path = "git_Insurance_ChatBot_demo_app/logbook/logbook.csv"

#log_database = pd.read_csv(log_book_path)
st.write(current_log_book)

