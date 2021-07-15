import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('parag2c.png')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.document_text_detection(image=image)
labels = response.full_text_annotation
#document_text_annotations
#label_annotations

print('Labels:')
#for label in labels:
print(labels.text)