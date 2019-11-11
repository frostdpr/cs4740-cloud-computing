import boto3
import os

s3 = boto3.resource('s3')

dirs = ['malathi','feng','sherriff']

# Get list of objects for indexing
images=[]

for dir_string in dirs:
  directory = os.fsencode(dir_string)

  for file in os.listdir(directory):
      
      filename = os.fsdecode(file)
      filepath = os.path.join(dir_string, filename)
      images.append((filepath, dir_string, filename))

      
# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('uva-professors-faces','index/'+ image[2])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )
