from google import genai

import os

from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)


def note_generator(images):

    prompt = """Summarize the picture in note format in language Bangla at max 100 words
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model= "gemini-3-flash-preview",
        contents=[ images, prompt]
    )

    return response.text