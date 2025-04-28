import json
import fastapi 
from file_handling import FileHandler
from bookGeneration import generate as bookGenerate
from contentGeneration import generate as contentGenerate
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://authorai.netlify.app"],  # Allow both local and production URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/")
def call(topic: str = fastapi.Body(...)) :
    print("Started Generating Book for : " + topic)
    content = contentGenerate(topic)
    
    print(content)
    res = bookGenerate(content)
    print(res)
    
    book_title = json.loads(res)['title'].replace(" ", "_")
    file = FileHandler(f"./cache/")
    file.write_file(f"{book_title}.json", res)
    print("Completed Generating Book for : " + topic)
    return res

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 2384)
    # print(call("Photosynthesis"))
