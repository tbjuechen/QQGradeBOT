import os
import random

from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

PHOTOPATH = os.path.join(os.path.expanduser('~'),'Downloads','集美')


def choose_random_file(directory):
    file_list = os.listdir(directory)
    random_file = random.choice(file_list)
    return random_file


@app.get('/photo')
def push_photo():
    random_file = choose_random_file(PHOTOPATH)
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