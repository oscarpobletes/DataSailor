# Oscar Poblete Sáenz
import streamlit as st # Build the app
import pandas as pd # Load data 
from pandasai import PandasAI # Analyze with pandas AI
from apikey import apikey # Use OpenAI API key
from pandasai.llm.openai import OpenAI # Build LLM workflow
import os # Interact with the file system
import glob # Locate files in a directory

# API key
openai_api_key = apikey

# Language model
llm = OpenAI(api_token = openai_api_key)
pandas_ai = PandasAI(llm, save_charts = True, save_charts_path = "./")

# Configuration
st.set_page_config(
    page_title = "DataSailor",
    page_icon = "⛵",
)

# Load CSV data
data_path = 'movie_metadata.csv' # Retrieved from: https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset
df = pd.read_csv(data_path)
st.session_state.df = df

# Initialize session state variables
if 'latest_chart_file' not in st.session_state:
    st.session_state.latest_chart_file = None

# App content
st.markdown("<h1 style='text-align: center;'>⛵ DataSailor</h1>", unsafe_allow_html=True)
st.markdown("""
<p style="text-align: center;"><i>Navigate your data effortlessly!</i> <br><br>
With DataSailor, you can explore and analyze your data with ease. Input your queries below and let me assist you in discovering insights from your dataset.<br></p>
""", unsafe_allow_html = True)

# Display Dataframe
st.dataframe(df, use_container_width = True)

# Prompt
prompt = st.text_area("Enter your prompt:")

if prompt:
    with st.spinner("Generating response..."):    
        # Run the AI model
        answer = pandas_ai.run(st.session_state.df, prompt)

        # List all chart.png files in subdirectories
        chart_files = glob.glob('./exports/charts/*/chart.png')
        
        # Determine the most recent chart file
        latest_chart_file = max(chart_files, key=os.path.getctime, default=None)
        
        # Check if there is a new chart to display
        if latest_chart_file and latest_chart_file != st.session_state.latest_chart_file:
            st.session_state.latest_chart_file = latest_chart_file
            st.image(latest_chart_file, use_column_width=True)
        else:
            # Display the answer if no new chart or no chart found
            st.write(answer)