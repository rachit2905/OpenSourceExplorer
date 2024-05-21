# OpenSourceExplorer

OpenSourceExplorer is a chatbot designed to help you find the right GitHub repository for your needs. It leverages RAG and LLM models, integrated with GitHub's APIs.

## Prerequisites

- Python 3.8 or later
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**
GPT
Certainly! Here's a streamlined README.md content designed to be clear and easy to follow for anyone looking to set up and run the OpenSourceExplorer project:

# OpenSourceExplorer

OpenSourceExplorer is a chatbot designed to help you find the right GitHub repository for your needs. It leverages RAG and LLM models, integrated with GitHub's APIs.

## Prerequisites

- Python 3.8 or later
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**
git clone https://github.com/yourusername/OpenSourceExplorer.git
cd OpenSourceExplorer

2. **Create and Activate Virtual Environment**

- **Windows:**
  ```
  python -m venv venv
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

3. **Install Dependencies**

   pip install -r requirements.txt

   4. **Environment Variables**
- Create a `.env` file in the project root.
- Add necessary API keys:
  ```
  API_KEY='YOUR_API_KEY_HERE'
  ```

5. **Run the Application**

6. streamlit run app.py
