# ai_service.py
import google.generativeai as genai
import os

# load your API key (you can set env variable GEMINI_API_KEY)
genai.configure(api_key='AIzaSyCzwU2KLIMck8n2OV-FJWKZ5V0oQhLK6oI')

model = genai.GenerativeModel("gemini-2.0-flash-lite")

def analyze_sentiment(text: str):
    prompt = f"""
    Analyze the following text and respond with just text nothing else:
    - sentiment: Positive, Negative, or Neutral
    Text: {text}
    """

    response = model.generate_content(prompt)

    return response.text  # plain text output


def analyze_text(text: str):
    prompt = f"""
    Analyze the following text and summarize it in 1-2 sentences
    Text: {text}
    """

    response = model.generate_content(prompt)

    return response.text  # plain text output


def analyze_emotion(text: str):
    prompt = f"""
    Analyze the following text and identify the emotion in it
    Text: {text}
    """

    response = model.generate_content(prompt)

    return response.text  # plain text output


def summarize_all_comments(comments: list[str]):
    text_block = "\n".join([f"- {c}" for c in comments])

    prompt = f"""
    Summarize all the following comments into one single concise paragraph:

    {text_block}
    """

    response = model.generate_content(prompt)
    return response.text
