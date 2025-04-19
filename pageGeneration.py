import json
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()
def generate(content_number, content_title, content_summary, total_words):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f'''
                    Content Number: {content_number}
                    Content Title: {content_title}
                    Content Summary: {content_summary}
                    Total Words: {total_words}
                '''),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["content_number", "content_title", "content"],
                        properties = {
                            "content_number": genai.types.Schema(
                                type = genai.types.Type.NUMBER,
                            ),
                            "content_title": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "content": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        },
                    ),
        system_instruction=[
            types.Part.from_text(text="""You are Althor (AI + Author) (AI Book Generation Model). Your job is to generate content body. You will be provided with the content number, title, summary and total words."""),
        ],
    )

    response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response += chunk.text
    return response

if __name__ == "__main__":
    res = generate("1", "Photosynthesis", "Photosynthesis is the process by which plants convert sunlight into energy.", "1000")
    print(json.loads(res))