import os
import random

from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import cv2 

# 加载Haar级联分类器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


app = FastAPI()

PHOTOPATH = os.path.join(os.path.expanduser('~'),'Downloads','beauty')

def is_hear_photo(url: str)->bool:
    img = cv2.imread(url)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    print(len(faces))
    return len(faces)>0

def choose_random_file(directory):
    file_list = os.listdir(directory)
    random_file = random.choice(file_list)
    return random_file


@app.get('/photo')
def push_photo():
    while (True):
        random_file = choose_random_file(PHOTOPATH)
        file_path = os.path.join(PHOTOPATH,random_file)
        if is_hear_photo(file_path):
            break

    with open(os.path.join(PHOTOPATH,random_file), 'rb') as f:
        photo = f.read()
    return Response(content=photo, media_type="image/jpeg")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run('test:app', host="127.0.0.1", port=8888, reload=True, workers=1)