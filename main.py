from contentGeneration import generate as contentGenerate 
from file_handling import FileHandler
import json

def generateBook(topic) :
    contents = json.loads(contentGenerate(topic))
    FileHandler("content.json").write_file(json.dumps(contents, indent=4))
    

if __name__ == "__main__" :
    topic = input("Enter Topic : ")    
    generateBook(topic)