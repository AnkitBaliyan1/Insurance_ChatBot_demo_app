import streamlit as st
#import os
from openai._client import OpenAI
import time
import pandas as pd
import os

API_KEY = st.secrets['OPENAI_API']

current_log_book = pd.DataFrame(columns=['user','time','question','answer'])
log_book_path = "/logbook/logbook.csv"

log_database = pd.read_csv(log_book_path)

with open(log_book_path,'rb') as file:
    df = file.read()


def database_app():
    st.write(df)
    
