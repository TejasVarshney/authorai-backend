import json
import fastapi 
import os
from file_handling import FileHandler
from bookGeneration import generate as bookGenerate
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with your Netlify URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def call(topic: str = fastapi.Body(...)) :
    print("Started Generating Book for : " + topic)
    res = bookGenerate(topic)
    
    book_title = json.loads(res)['title'].replace(" ", "_")
    file = FileHandler(f"./cache/")
    file.write_file(f"{book_title}.json", res)
    print("Completed Generating Book for : " + topic)
    return res

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)