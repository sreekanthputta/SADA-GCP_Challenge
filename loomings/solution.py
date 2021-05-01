from minio import Minio
from minio.error import S3Error
from hashlib import sha256
import io
import math
import collections
import os




#Connection to Minio Server
client = Minio(
    "35.202.171.168:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

# Make 'loomings' bucket if not exist.
found = client.bucket_exists("loomings")
if not found:
    client.make_bucket("loomings")
else:
    print("Bucket 'loomings' already exists")
    
#Push loomings.txt fileto bucket
client.fput_object("loomings", "loomings.txt", 'loomings.txt')
print("'loomings.txt' is successfully uploaded as object 'loomings.txt' to bucket 'loomings'.")




#Read each line from loomings.txt and push each line as a file to the bucket including the metadata
with open('loomings.txt', 'r',encoding='utf-8') as loomings:
    lines = loomings.readlines()
    fileCount = 0
    for line in lines:
        strippedLine = line.strip()
        if(len(strippedLine)>0):
            strippedLine = strippedLine.encode('utf-8')
            fileCount += 1
            filename = "File-"+str(fileCount)
            #I have used SHA256 to find the hash of the file
            hash = sha256(strippedLine).hexdigest()
            length = len(strippedLine)
                        
            #put_object is used to create a file with a string.
            client.put_object(
                "loomings", filename, io.BytesIO(bytes(strippedLine)), length, metadata={"Content-hash": hash},
            )
            print(filename, " is successfully uploaded to bucket 'loomings' with metadata ", {"Content-hash": hash})
            

#Printing the numbe of non blank lines using the counter variable fileCount
print("\nTotal number of Non blank lines : ", str(fileCount))




#Finding the size of all files using list_objects
fileSizeMap = []
for file in client.list_objects('loomings'):
    filename = file.object_name
    if('File-' in filename):
        fileSizeMap.append([filename, file.size])
                
#Sorting the list according the size of each file
print("List of files and their sizes in ascending order:")
fileSizeMap.sort(key=lambda x: x[1])
for fileSize in fileSizeMap:
    print("FileName : "+fileSize[0].rjust(8)+",    File Size : "+str(fileSize[1]).rjust(4))



#Method to get file content using the fget_object 
def getFileContent(fileName):
    client.fget_object('loomings', fileName, fileName)
    with open(fileName, 'r',encoding='utf-8') as file:
        line = file.readline().strip()
    os.remove(fileName)
    return line
                
#Creating a hashmap with hash as key and list of files as value.
hashFilesMap = collections.defaultdict(list)
for file in client.list_objects('loomings'):
    if('File-' in file.object_name):
        fileName = file.object_name
        fileInfo = client.fget_object('loomings', fileName, fileName)
        hash = fileInfo.metadata['x-amz-meta-content-hash']
        os.remove(fileName)
        hashFilesMap[hash].append(fileName)
    
#If there are multiple files with the same hash, then they are duplicates. So just keep one of them. 
for files in hashFilesMap.values():
    if(len(files)>1):
        print(', '.join(files), "have the same hash digest.")
        print("\nThe original text line of "+files[0]+": ", getFileContent(files[0]))
        
#Variable to store the list of line numbers to be deleted as they are duplicates.
deleteLines = list()

for files in hashFilesMap.values():
    if len(files)>1:
        deleteLines.extend([x.replace('File-', '') for x in files[1:]])
        
print("\nLines", ','.join(deleteLines), "will be removed from 'loomings.txt' as they are duplicates.")

#Create a new file with all the lines from loomings.txt except for the duplicates
with open('loomings.txt', 'r',encoding='utf-8') as loomings:
    with open('loomings-clean.txt', 'w', encoding='utf-8') as clean:
        clean.truncate(0)
        lines = loomings.readlines()
        j = 0
        for i, line in enumerate(lines):
            if(len(line.strip())>0):
                j += 1
                if(j not in deleteLines):
                    clean.write(str(line))
                    if(i!=len(lines)-1): clean.write("\n")
print("'loomings-clean.txt' has been generated with unique statements")

