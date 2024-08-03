# DataSailor

Data Sailor is an interactive app built with Streamlit to help you navigate and analyze your datasets effortlessly. Powered by OpenAI's language model (LLM) and PandasAI, it enables you to input natural language queries and receive insightful analyses directly from your data.

## Features

- **User-Friendly Interface:** Explore any dataset with ease using a simple and intuitive interface.
- **Natural Language Queries:** Uncover valuable insights using everyday language.
- **Data Visualization:** Interpret data trends and patterns with diverse charts and graphs.


## Installation

To run DataSailor locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/oscarpobletes/DataSailor.git
   cd DataSailor
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Modify the data_path variable in `app.py` to reference your dataset in CSV format:

     ```python
     data_path = 'YOUR_DATASET_FILENAME.csv'
     ```

 
4. Insert your active [OpenAI API key](https://platform.openai.com/api-keys) into `apikey.py`:

     ```python
     apikey = 'YOUR_OPENAI_API_KEY'
     ```

5. Run the application:

     ```bash
     streamlit run app.py
     ```

You're all set to sail! Just wait for a new window to open automatically or visit localhost:8501 in your web browser.

## Note

Data Sailor uses PandasAI library version 0.8.4. For details on updates and releases, visit the [PandasAI GitHub repository](https://github.com/Sinaptik-AI/pandas-ai/releases?page=12).