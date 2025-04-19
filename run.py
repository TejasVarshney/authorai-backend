from contentGeneration import generate as contentGenerate 
from pageGeneration import generate as pageGenerate
from file_handling import FileHandler
import json

def generateBook(topic) :
    # generate contents for the book
    file = FileHandler(f"./cache/{topic}")
    
    contents = json.loads(contentGenerate(topic))
    file.write_file("contents.json", json.dumps(contents, indent=4))
    
    # generate content body for each content in contents
    for(content) in contents["contents"] :
        print(str(content["content_number"]) + " " + content["content_title"] + " : on process")
        
        #generate the content body for each title 
        page = json.loads(pageGenerate(content["content_number"], content["content_title"], content["content_summary"], content["total_words"]))
        
        #write a json file for each content
        file.write_file(str(content["content_number"]) + ".json", json.dumps(page, indent=4))
        
        #write a markdown file for each content
        file.write_file(topic + str(content["content_number"]) + ".md", page["content_title"] + "\n")
        file.append_file(topic + str(content["content_number"]) + ".md", page["content"])
        
        print(str(content["content_number"]) + " " + content["content_title"] + " : done")

if __name__ == "__main__" :
    topic = input("Enter Topic : ")    
    generateBook(topic)