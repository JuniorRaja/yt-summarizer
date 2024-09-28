
# YouTube Summarizer API

This project is a Flask-based API that extracts transcripts from YouTube videos and summarizes them using the OpenAI API. The API provides a simple endpoint to handle video summarization requests.

## Features

- Extracts transcripts from YouTube videos using the `youtube-transcript-api`.
- Summarizes the transcript with OpenAI's GPT-3.5 model.
- Provides a RESTful API endpoint for easy integration.

## Requirements

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- `pip` (Python package manager)

## Installation

1. **Clone the repository** (or create a new directory):

   ```bash
   git clone https://github.com/yourusername/youtube-summarizer.git
   cd youtube-summarizer
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install the required packages**:

   ```bash
   pip install Flask requests youtube-transcript-api openai python-dotenv
   ```

4. **Set up environment variables**:

   - Create a file named `.env` in the project directory.
   - Add your OpenAI API key to the `.env` file:

     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

   Make sure to replace `your_openai_api_key_here` with your actual OpenAI API key.

5. **Add `.env` to `.gitignore`**:

   To avoid accidentally pushing your sensitive API key to a public repository, create a `.gitignore` file and add `.env` to it:

   ```
   .env
   ```

## Usage

1. **Run the Flask application**:

   ```bash
   python app.py
   ```

   The API will start and listen on `http://127.0.0.1:5000`.

2. **Make a POST request to the `/summarize` endpoint**:

   You can use tools like `curl`, Postman, or any HTTP client to make requests.

   Example request using `curl`:

   ```bash
   curl -X POST http://127.0.0.1:5000/summarize \
   -H "Content-Type: application/json" \
   -d '{"video_url": "https://www.youtube.com/watch?v=your_video_id_here"}'
   ```

   Replace `your_video_id_here` with the actual ID of the YouTube video you want to summarize.

3. **Response**:

   The API will respond with a JSON object containing the summary:

   ```json
   {
       "summary": "This is a summary of the video..."
   }
   ```

## Error Handling

The API handles errors gracefully and will return appropriate HTTP status codes and messages for common issues:

- **400 Bad Request**: Returned when the video URL is missing or if the transcript cannot be retrieved.
- **500 Internal Server Error**: Returned for unexpected errors.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - A micro web framework for Python.
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) - For fetching YouTube video transcripts.
- [OpenAI API](https://openai.com/api/) - For text summarization using GPT models.
