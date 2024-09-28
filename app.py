from flask import Flask, request, jsonify
from services.youtubeAPI import get_transcript
from services.openaiAPI import summarize_text
from utils.helpers import extract_video_id

# Initialize Flask app
app = Flask(__name__)

# API endpoint to handle YouTube summarization
@app.route('/summarize', methods=['POST'])
def summarize_video():
    data = request.get_json()
    video_url = data.get('video_url')
    
    if not video_url:
        return jsonify({"error": "Please provide a YouTube video URL"}), 400

    try:
        video_id = extract_video_id(video_url)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    # Get the transcript of the YouTube video
    transcript = get_transcript(video_id)
    if "Error retrieving transcript" in transcript:
        return jsonify({"error": transcript}), 400

    # Summarize the transcript using OpenAI API
    summary = summarize_text(transcript)
    
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
