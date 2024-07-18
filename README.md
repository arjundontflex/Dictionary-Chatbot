# Dictionary Chatbot

This is a simple dictionary chatbot application built with Streamlit. The chatbot fetches word definitions from the Oxford Dictionary API and displays them to the user.

## Project Structure

project_directory/
│
├── app.py # Main application code
├── requirements.txt # Required Python packages
├── templates/
│ └── index.html # HTML template for the UI
└── static/
└── style.css # CSS for styling the UI


## Requirements

- Python 3.7 or higher
- Streamlit
- Requests

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/dictionary-chatbot.git
    cd dictionary-chatbot
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://localhost:8501
    ```

## Usage

1. **Enter a word in the input field.**
2. **Click Enter and wait for the definition to be displayed.**

## Project Components

- `app.py`: Contains the main Streamlit application code.
- `templates/index.html`: Contains the HTML structure of the application.
- `static/style.css`: Contains the CSS for styling the application.

## License

This project is licensed under the MIT License.
