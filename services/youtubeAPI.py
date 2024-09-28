from youtube_transcript_api import YouTubeTranscriptApi

# Function to extract transcript from YouTube
def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([entry['text'] for entry in transcript_list])
        return transcript
    except Exception as e:
        return f"Error retrieving transcript: {str(e)}"
