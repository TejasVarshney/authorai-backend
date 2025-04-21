import base64
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate(topic):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=topic),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""Your AI Author Assistance. Your job is to take prompt and based on the prompt give the title of the, list of Chapter with chapter number and title, total page in each chapter, chapter summary. (Overall pages must be in range of 5-10). Your response will be feed to another AI."""),
        ],
    )

    res = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        res += chunk.text

    return res

if __name__ == "__main__":
    print(generate())
