# Method 1 : Custom Handling
class Open_File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self,exc_type, exc_val, traceback):
        self.file.close()
        
        
with Open_File('sample.txt','w') as file:
    file.write('Lorem Ipsum')
    
print(file.closed)

#Method 2
from contextlib import contextmanager

@contextmanager
def open_file(filename,mode):
    file = open(filename, mode)
    yield file
    file.close()
    
    
with open_file('sample.txt','w') as file:
    file.write('Lorem Ipsum')
    
    
print(file.closed)