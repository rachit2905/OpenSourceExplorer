# OpenSourceExplorer

OpenSourceExplorer is a chatbot designed to help you find the right GitHub repository for your needs. It leverages Retrieval-Augmented Generation (RAG) and Large Language Models (LLM), integrated with GitHub's APIs.

##Demo
(https://github.com/rachit2905/OpenSourceExplorer/assets/85569226/0627d093-c51a-4ea5-ae5b-51e056b7680d)

## Prerequisites

- Python 3.8 or later
- pip (Python package installer)

## Setup Instructions

1. **Clone the Repository**
   - Clone the repository to your local machine and navigate to the project directory.

2. **Create and Activate Virtual Environment**
   - Set up a virtual environment to manage dependencies.

3. **Install Dependencies**
   - Install the required Python packages listed in `requirements.txt`.

4. **Environment Variables**
   - Create a `.env` file in the project root and add the necessary API keys.
     ```
     API_KEY='YOUR_API_KEY_HERE'
     ```

5. **Run the Application**
   - Start the Streamlit application.

## Features

### 🚀 Open Source Explorer: Discover Awesome GitHub Repositories

OpenSourceExplorer is built using the Retrieval-Augmented Generation (RAG) framework, leveraging Google's Generative AI model Gemini-PRO. It processes knowledge from specific open-source GitHub repositories and provides accurate recommendations based on user queries. This advanced approach ensures high-quality, contextually relevant responses for an efficient and effective user experience.

### 🔍 How It Works

1. **PDF Processing**: The system processes the PDF document located in the data directory to extract relevant information about GitHub repositories.
2. **Ask a Question**: Users can ask any question related to open-source repositories and get precise recommendations.

### User Interface

- **Custom CSS**: The application includes custom CSS for a dark theme and enhanced font styles, ensuring a visually appealing user interface.
- **Interactive Input**: Users can interact with the chatbot by entering their queries in the provided text input field.

### Technical Details

- **PDF Text Extraction**: Utilizes PyPDF2 for extracting text from PDF documents.
- **Text Splitting**: Uses LangChain's RecursiveCharacterTextSplitter to handle large chunks of text.
- **Embeddings and Vector Store**: Integrates GoogleGenerativeAIEmbeddings and FAISS for creating and managing vector stores.
- **Conversational Chain**: Employs a custom prompt template and Google's Generative AI for generating responses to user queries.

## Steps to Run the Project

1. **Clone the Repository**
   - Clone the repository to your local machine and navigate to the project directory.
     ```sh
     git clone https://github.com/rachit2905/OpenSourceExplorer.git
     cd OpenSourceExplorer
     ```

2. **Create and Activate Virtual Environment**
   - Set up a virtual environment to manage dependencies.
     - **Windows:**
       ```sh
       python -m venv venv
       venv\Scripts\activate
       ```
     - **macOS/Linux:**
       ```sh
       python3 -m venv venv
       source venv/bin/activate
       ```

3. **Install Dependencies**
   - Install the required Python packages listed in `requirements.txt`.
     ```sh
     pip install -r requirements.txt
     ```

4. **Environment Variables**
   - Create a `.env` file in the project root and add the necessary API keys.
     ```sh
     echo "API_KEY='YOUR_API_KEY_HERE'" > .env
     ```

5. **Run the Application**
   - Start the Streamlit application.
     ```sh
     streamlit run app.py
     ```



