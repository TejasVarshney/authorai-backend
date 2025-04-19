import os
import shutil
import random

class FileHandler :
    def __init__(self, folder_dir):
        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)
        else :
            shutil.rmtree(folder_dir)
            os.makedirs(folder_dir)
        self.file_path = folder_dir

    def read_file(self, file_name) :
        with open(self.file_path+"/"+file_name, 'r') as f :
            return f.read()
    
    def write_file(self, filename, content) :
        with open(self.file_path+"/"+filename, 'w') as f :
            f.write(content)
    
    def append_file(self, filename, content) :
        with open(self.file_path+"/"+filename, 'a') as f :
            f.write(content)
            
    def delete_file(self, filename) :
        import os
        os.remove(self.file_path+"/"+filename)
        
if __name__ == "__main__" :
    f = FileHandler("./cache/photosynthesis", "contents.json")
    f.write_file('{"contents":[{"content_number":1,"content_title":"Photosynthesis","content_summary":"Photosynthesis is the process by which plants convert sunlight into energy.","total_words":1000}]}')
    print(f.read_file())