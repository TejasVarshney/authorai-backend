import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

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
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["contents"],
                        properties = {
                            "contents": genai.types.Schema(
                                type = genai.types.Type.ARRAY,
                                items = genai.types.Schema(
                                    type = genai.types.Type.OBJECT,
                                    required = ["content_number", "content_title", "content_summary", "total_words"],
                                    properties = {
                                        "content_number": genai.types.Schema(
                                            type = genai.types.Type.NUMBER,
                                        ),
                                        "content_title": genai.types.Schema(
                                            type = genai.types.Type.STRING,
                                        ),
                                        "content_summary": genai.types.Schema(
                                            type = genai.types.Type.STRING,
                                        ),
                                        "total_words" : genai.types.Schema(
                                            type = genai.types.Type.NUMBER
                                        )
                                    },
                                ),
                            ),
                        },
                    ),
        system_instruction=[
            types.Part.from_text(text="""You are my AI Book Generation Model for content Generation. You job is to generate contents with summary for book based on the given topic."""),
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

# if __name__ == "__main__":
#     generate()
