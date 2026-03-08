from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from TTS.api import TTS
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

@app.post("/clone")
async def clone(voice: UploadFile, text: str = Form(...)):

    with open("voice.wav", "wb") as buffer:
        shutil.copyfileobj(voice.file, buffer)

    tts.tts_to_file(
        text=text,
        speaker_wav="voice.wav",
        language="pt",
        file_path="output.wav"
    )

    return FileResponse("output.wav")
