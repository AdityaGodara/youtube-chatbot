# filepath: youtube-chatbot/README.md
# YouTube Chatbot Project

## Overview
The YouTube Chatbot is a conversational application built using Streamlit that allows users to interact with YouTube video transcripts. It utilizes the Langchain library to create a vector database from video transcripts and generate responses based on user queries.

## Project Structure
```
youtube-chatbot
├── src
│   ├── langchain_helper.py      # Functions for creating vector databases and generating responses
│   ├── app.py                    # Main entry point for the Streamlit application
│   ├── utils
│   │   └── config.py             # Configuration settings and environment variable loading
│   └── styles
│       └── main.css              # Custom CSS styles for the Streamlit application
├── requirements.txt              # List of dependencies for the project
├── .env                           # Environment variables for configuration
└── README.md                     # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add any necessary environment variables.

## Usage
To run the Streamlit application, execute the following command:
```
streamlit run src/app.py
```

## Features
- Load YouTube video transcripts and create a vector database.
- Generate responses to user queries based on video content.
- User-friendly interface built with Streamlit.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.