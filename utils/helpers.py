# Function to extract the video ID from a YouTube URL
def extract_video_id(video_url):
    try:
        if 'v=' in video_url:
            return video_url.split('v=')[-1].split('&')[0]  # Supports additional parameters after 'v='
        elif 'youtu.be/' in video_url:
            return video_url.split('youtu.be/')[-1]  # Handle shortened YouTube URLs
        else:
            raise ValueError("Invalid YouTube URL format.")
    except Exception as e:
        raise ValueError(f"Error extracting video ID: {str(e)}")
