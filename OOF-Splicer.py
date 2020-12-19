import pickle
import sys
import os

mb=8192000 # Size to split files into

class out:
    def __init__(self, name):
        self.name=name

def make(start, end, i, data): # Function for creating split files
    print('Generating OOF '+str(i+1)+'...')
    
    if end > len(data):
        end=len(data)
    f=open('S'+str(i+1)+'.OOF','wb')
    
    for i in range(start, end):
        f.write(bytes([data[i]]))
    f.close()
    
if __name__ == '__main__':
        index=out(os.path.basename(sys.argv[1])) # Get filename from full path
        file=open(sys.argv[1], 'rb')
        data=pickle.dumps(file.read())
        file.close()
        form=open('S0.OOF', 'wb')
        form.write(pickle.dumps(index)) # Dump filename to S0.OOF
        form.close()
        num=int(len(data)/mb)+1
        print('Generating '+str(num+1)+ ' OOF\'s...')
        print('Generating OOF 0...')
        for i in range(0,num):
            make(i*mb, i*mb+mb, i, data) # Create split files
