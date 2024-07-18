import streamlit as st
import requests

# Oxford Dictionary API credentials
rapidapi_key = '97e3139a3cmsh644ef8adadf9762p16097fjsnf5403961d00c'
rapidapi_host = 'joughtred-oxford-dictionaries-v1.p.rapidapi.com'

# Function to get word definition from Oxford Dictionary API via RapidAPI
def get_definition(word):
    url = f"https://{rapidapi_host}/entries/en-us/{word}/examples"
    headers = {
        "x-rapidapi-key": rapidapi_key,
        "x-rapidapi-host": rapidapi_host
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        definitions = []
        if 'results' in data:
            for entry in data['results']:
                if 'lexicalEntries' in entry:
                    for lexicalEntry in entry['lexicalEntries']:
                        if 'entries' in lexicalEntry:
                            for sense in lexicalEntry['entries']:
                                if 'senses' in sense:
                                    for definition in sense['senses']:
                                        if 'definitions' in definition:
                                            definitions.append(definition['definitions'][0])
        return definitions if definitions else ["No definition found."]
    else:
        return ["Error fetching definition from Oxford Dictionary API."]

# Read HTML and CSS files
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Streamlit UI
html_content = read_file('templates/index.html')
css_content = read_file('static/style.css')

# Inject CSS and HTML into Streamlit
st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
st.markdown(html_content, unsafe_allow_html=True)

# User input for word definition
user_input = st.text_input("Enter a word:")

if user_input:
    with st.spinner("Looking up the word..."):
        definitions = get_definition(user_input)
        st.write("Definitions:")
        for definition in definitions:
            st.write(f"- {definition}")
