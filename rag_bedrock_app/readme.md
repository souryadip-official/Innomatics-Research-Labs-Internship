# Enterprise Knowledge Base Q&A System (RAG)

## Overview
This project is a Question-Answering system built using Amazon Bedrock Knowledge Bases.

It allows users to ask questions in natural language and get answers from internal company documents.

## What we are doing
- Taking user question from Streamlit UI
- Sending it to Amazon Bedrock
- Retrieving relevant data from Knowledge Base (vector search)
- Generating answer using LLM
- Showing answer along with sources

## Tech Used
- Python
- Streamlit
- Amazon Bedrock
- AWS S3
- EC2

## How to Run
pip install -r requirements.txt
streamlit run app.py

## Note
- Uses private company data
- Answers are based on retrieved documents (RAG)