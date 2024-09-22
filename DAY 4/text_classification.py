import cv2
import pytesseract
from PIL import Image
from easyocr import Reader
import boto3
import os


reader = Reader(['en'])

def read_text_tesseract(image_path):

  text = pytesseract.image_to_string(Image.open(image_path), lang='eng')
  return text

def read_text_easyocr(image_path):
  text = ''
  results = reader.readtext(Image.open(image_path))
  for result in results:
    text = text + result[1] +  ' '

  text = text[:-1]
  return text


def jaccard_similarity(sentence1, sentence2):
    # Tokenize sentences into sets of words
    set1 = set(sentence1.lower().split())
    set2 = set(sentence2.lower().split())

    # Calculate Jaccard similarity
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))

    # Avoid division by zero if both sets are empty
    similarity = intersection_size / union_size if union_size != 0 else 0.0

    return similarity



score_tesseract = 0
score_easyocr = 0

for image_path_ in os.listdir('/content/data'):
  image_path = os.path.join('/content/data', image_path_)

  gt = image_path[:-4].replace('_', ' ').lower()

  score_tesseract += jaccard_similarity(gt, read_text_tesseract(image_path).lower().replace('\n', '').replace('!', '').replace('?', '').replace('.', ''))
  score_easyocr += jaccard_similarity(gt, read_text_easyocr(image_path).lower().replace('\n', '').replace('!', '').replace('?', '').replace('.', ''))
  

print('score tesseract:', score_tesseract / 100)
print('score_easyocr:', score_easyocr / 100)
