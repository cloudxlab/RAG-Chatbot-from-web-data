# Building a Custom Chatbot from Your Website Data using OpenAI and Langchain

This project enables you to build a custom RAG based chatbot that answers customer queries using website data. The chatbot utilizes ChatGPT and LangChain to answer user questions based on the content of a specified website.

## Setup Instructions

Follow these steps to set up the project on your local machine:

1. **Clone the Repository:**
   ```
   git clone https://github.com/cloudxlab/RAG-Chatbot-from-web-data.git
   ```

2. **Create a Virtual Environment:**

   Note: We used Python 3.10.11 to create the virtual environment. Please ensure that you use the same Python version to avoid potential conflicts and ensure compatibility with the project dependencies.
   ```
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment:**
   ```
   . venv/bin/activate
   ```

5. **Install Requirements:**
   ```
   pip install -r requirements.txt
   ```

6. **Configure Environment Variables:**
   - Rename `env_sample.sh` to `env.sh`.
   - Add your OpenAI API key to `env.sh`:
     ```
     export OPENAI_API_KEY="your_openai_api_key_here"
     ```

## Usage

Once the project is set up, you can proceed to run the demo code provided in `demo.ipynb` to see the chatbot in action.

## Video explanation

Please find the video explanation [here](https://youtube.com/live/RMt7UaVs33A).

## Further Work

To enhance the capabilities of the chatbot and improve its usability, the following tasks can be implemented:

### 1. Crawl Whole Sitemap and Store in Vector Store

Extend the functionality of the chatbot to crawl entire sitemaps of websites and store the relevant information in a vector store. This would allow the chatbot to access a broader range of data and provide more comprehensive responses to user queries.

### 2. Automate the Web Crawling Process

Implement automation for the web crawling process to streamline data collection and update procedures. This automation can include scheduling regular crawls to ensure that the chatbot's knowledge base remains up-to-date with the latest content from the target website(s).

These enhancements will improve the chatbot's efficiency, accuracy, and ability to provide relevant information to users based on the data available on the website(s).
