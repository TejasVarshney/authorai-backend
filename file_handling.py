class FileHandler :
    def __init__(self, file_path) :
        self.file_path = file_path
        
    def read_file(self) :
        with open(self.file_path, 'r') as f :
            return f.read()
    
    def write_file(self, content) :
        with open(self.file_path, 'w') as f :
            f.write(content)
    
    def append_file(self, content) :
        with open(self.file_path, 'a') as f :
            f.write(content)
            
    def delete_file(self) :
        import os
        os.remove(self.file_path)