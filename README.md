# ResearchPipelineAgent-ADK
This Repositories is Providing How to Deploy Agent using Agent Development Kit.
Agent Development Kit (ADK)
This repository contains examples for learning Google's Agent Development Kit (ADK), a powerful framework for building LLM-powered agents.

Getting Started
Setup Environment
You only need to create one virtual environment for all examples in this course. Follow these steps to set it up:

### Create virtual environment in the root directory
python -m venv .venv

### Activate (each new terminal)
### macOS/Linux:
source .venv/bin/activate
### Windows CMD:
.venv\Scripts\activate.bat
### Windows PowerShell:
.venv\Scripts\Activate.ps1

### Install dependencies
pip install -r requirements.txt
Once set up, this single environment will work for all examples in the repository.

### Setting Up API Keys
Create an account in Google Cloud https://cloud.google.com/?hl=en
Create a new project
Go to https://aistudio.google.com/apikey
Create an API key
Assign key to the project
Connect to a billing account
Each example folder contains a .env.example file. For each project you want to run:

Navigate to the example folder
Rename .env.example to .env
Open the .env file and replace the placeholder with your API key:
GOOGLE_API_KEY=your_api_key_here
You'll need to repeat this for each example project you want to run.

Examples Overview
Here's what you can learn from each example folder:

1. Basic Agent
Introduction to the simplest form of ADK agents. Learn how to create a basic agent that can respond to user queries.

2. ResearchPipelineAgent-
introduction to the ResearchPipeline Agent where used google search used  as Tool.

3. Stateful Multi-Agent
Build agents that maintain and update state throughout complex multi-turn conversations.

4. Sequential Agent
Create pipeline workflows where agents operate in a defined sequence to process information.





Official Documentation
For more detailed information, check out the official ADK documentation:

https://google.github.io/adk-docs/get-started/quickstart



