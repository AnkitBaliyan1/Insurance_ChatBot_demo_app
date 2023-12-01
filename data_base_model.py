import streamlit as st
#import os
from openai._client import OpenAI
import time
import pandas as pd
import os

API_KEY = st.secrets['OPENAI_API']



def database_app():
    st.wirte("runing")
