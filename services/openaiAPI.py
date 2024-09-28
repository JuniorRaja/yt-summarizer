import openai
from config import OPENAI_API_KEY

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Function to summarize transcript using OpenAI
def summarize_text(transcript, max_tokens=150):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes YouTube video transcripts. Make sure to finish in 150 words."},
                {"role": "user", "content": f"Summarize the following text:\n\n{transcript}"}
            ],
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.5
        )
        summary = response.choices[0].message['content']
        return summary.strip()
    except openai.error.OpenAIError as e:
        return f"OpenAI API Error: {str(e)}"
    except Exception as e:
        return f"Error in summarization: {str(e)}"
