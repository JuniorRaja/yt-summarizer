from flask import Flask, request, jsonify
import requests
from youtube_transcript_api import YouTubeTranscriptApi
import openai

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Set your OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize Flask app
app = Flask(__name__)

# models = openai.Model.list()
# for model in models['data']:
#     print(model['id'])

# Function to extract transcript from YouTube
def get_transcript(video_url):
    try:
        video_id = video_url.split('v=')[-1]  # Extract video ID from URL
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([entry['text'] for entry in transcript_list])        
        return transcript
    except Exception as e:
        return str(e)

# Function to summarize transcript using OpenAI
def summarize_text(text):
      # Check if text is long enough to trim
    if len(text) > 500:
        trimmed_text = text[500:]  # Only trim if text is longer than 500 characters
    else:
        trimmed_text = text  # Use the full text if it's less than 500 characters

    try:
        response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Switch to gpt-3.5-turbo if gpt-4 is unavailable
    messages=[
        {"role": "system", "content": "You are a helpful assistant that summarizes YouTube video transcripts. Make sure to finish in 150 words."},
        {"role": "user", "content": f"Summarize the following text:\n\n{trimmed_text}"}
    ],
    max_tokens=150,
    n=1,
    stop=None,
    temperature=0.5
)
        # Print the full response for debugging
        print(response)
        
        # Access the content of the summary correctly
        summary = response.choices[0].message['content']
        return summary.strip()
    
    except Exception as e:
        return str(e)
    except openai.error.OpenAIError as e:
        return f"OpenAI API Error: {e}"

# API endpoint to handle YouTube summarization
@app.route('/summarize', methods=['POST'])
def summarize_video():
    data = request.get_json()
    video_url = data.get('video_url')
    
    if not video_url:
        return jsonify({"error": "Please provide a YouTube video URL"}), 400
    
    # Get the transcript of the YouTube video
    transcript = get_transcript(video_url)
    print(transcript)
    if "Could not retrieve a transcript" in transcript:
        return jsonify({"error": "Could not retrieve transcript for the video"}), 400
    
    # Summarize the transcript using OpenAI API
    summary = summarize_text(transcript)
    
    return jsonify({"summary": summary})

# Main entry point for the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Set Flask to run on port 5000
