import json
import fastapi 
from file_handling import FileHandler
from contentGeneration import generate as contentGenerate
from pageGeneration import generate as pageGenerate
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
    file = FileHandler(f"./cache/{topic}")
    
    contents = json.loads(contentGenerate(topic))
    file.write_file("contents.json", json.dumps(contents, indent=4))
    
    # generate content body for each content in contents
    res = []
    
    index = 0
    for(content) in contents["contents"] :
        print(str(content["content_number"]) + " " + content["content_title"] + " : on process")
        #generate the content body for each title 
        prevStory = ""
        if index > 0 :
            prevStory = res[index-1]["content"]
        page = json.loads(pageGenerate(content_number = content["content_number"], 
                                content_title = content["content_title"], 
                                content_summary = content["content_summary"], 
                                total_words = content["total_words"],
                                prevStory=prevStory
                                ))
        index += 1
        
        
        #write a json file for each content
        file.write_file(str(content["content_number"]) + ".json", json.dumps(page, indent=4))
        
        #write a markdown file for each content
        file.write_file(topic + str(content["content_number"]) + ".md", page["content_title"] + "\n")
        file.append_file(topic + str(content["content_number"]) + ".md", page["content"])
        
        res.append(page)
    
    return json.dumps({"response": res})

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run(app)