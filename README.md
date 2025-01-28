# Chatbot

## Food Recipe and Ingredient Chatbot
This repository contains the code for a chatbot application that provides recipes, ingredient lists, and cost estimates for various dishes. The chatbot is built using OpenAI's GPT API and is deployed with a user-friendly Streamlit interface.

### Features
Fetches recipes for any dish.
Lists ingredients with estimated costs.
Allows users to customize ingredients and costs based on local prices.
### Project Structure
chatbot.py: Contains the functions for interacting with the OpenAI API and fetching recipe data.
app.py: The main file for running the Streamlit application.
requirements.txt: Lists all the dependencies required to run the project.

### Installation and Setup
Prerequisites
Ensure you have the following installed:

Python (3.8 or higher)
Anaconda (optional, but recommended for managing environments)
Steps to Run
Clone the Repository

git clone https://github.com/your-repo-name.git
cd your-repo-name
Create a Virtual Environment (Optional but Recommended)
Using Anaconda:

conda create --name recipe_chatbot python=3.8
conda activate recipe_chatbot
Or using venv:

python -m venv env
source env/bin/activate  # Linux/Mac
.\env\Scripts\activate   # Windows
Install Dependencies

Set Up OpenAI API Key

OPENAI_API_KEY=your_openai_api_key
Run the Application
Open a terminal and run:
streamlit run app.py
Access the Application
The Streamlit app will open in your default web browser at http://localhost:8501.

## Common Errors and How I Solved Them
1. APIRemovedInV1 Error
What I Faced:
I encountered the error: APIRemovedInV1: You tried to access openai.Completion, but this is no longer supported in openai>=1.0.0.

How I Solved It:
The OpenAI Python library had updated to v1.0.0+, so I had to adjust my code to use the new syntax. I replaced openai.Completion.create() with client.chat.completions.create() as per the updated documentation. I also ensured my chatbot.py file reflected these changes.

2. Invalid Syntax Error
What I Faced:
While running my code, I got the error: SyntaxError: stream=True is invalid syntax.

How I Solved It:
This happened because I was using outdated syntax for OpenAI’s API. I updated the code to align with the library’s new requirements. Here’s the corrected example:


3. Streamlit Errors
What I Faced:
At one point, I saw the error: NameError: name 'st' is not defined.

How I Solved It:
I realized I had forgotten to import Streamlit in my app.py file. To fix this, I added the import at the beginning:
python
import streamlit as st

4. Dependency Issues
What I Faced:
Some libraries were missing, leading to ModuleNotFoundError errors.

How I Solved It:
I double-checked my requirements.txt file and ensured all dependencies were installed.
5. API Key Error
What I Faced:
When I tried running the application, I encountered the error: AuthenticationError: No API key provided.

How I Solved It:
I had forgotten to set my OpenAI API key. I fixed this by creating a .env file and adding the key:


