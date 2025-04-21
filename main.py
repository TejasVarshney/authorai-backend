import json
import fastapi 
from file_handling import FileHandler
from bookGeneration import generate as bookGenerate
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your React app's URL
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

# if __name__ == "__main__" :
#     import uvicorn
#     uvicorn.run(app)