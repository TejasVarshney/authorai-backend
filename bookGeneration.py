import base64
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
def generate(prompt):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["title", "total_pages", "total_chapters", "chapters", "category"],
                        properties = {
                            "title": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "total_pages": genai.types.Schema(
                                type = genai.types.Type.NUMBER,
                            ),
                            "total_chapters": genai.types.Schema(
                                type = genai.types.Type.NUMBER,
                            ),
                            "chapters": genai.types.Schema(
                                type = genai.types.Type.ARRAY,
                                items = genai.types.Schema(
                                    type = genai.types.Type.OBJECT,
                                    required = ["chapter"],
                                    properties = {
                                        "chapter": genai.types.Schema(
                                            type = genai.types.Type.ARRAY,
                                            items = genai.types.Schema(
                                                type = genai.types.Type.OBJECT,
                                                required = ["chapter_number", "page_number", "content", "chapter_name"],
                                                properties = {
                                                    "chapter_number": genai.types.Schema(
                                                        type = genai.types.Type.INTEGER,
                                                    ),
                                                    "page_number": genai.types.Schema(
                                                        type = genai.types.Type.NUMBER,
                                                    ),
                                                    "content": genai.types.Schema(
                                                        type = genai.types.Type.STRING,
                                                    ),
                                                    "chapter_name": genai.types.Schema(
                                                        type = genai.types.Type.STRING,
                                                    ),
                                                },
                                            ),
                                        ),
                                    },
                                ),
                            ),
                            "category": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        },
                    ),
        system_instruction=[
            types.Part.from_text(text="""You are Author that generate book based on the topic. Each page must contains atleast 500 words. Be creative on your writing style and make it engaging."""),
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
