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

# modelo mais leve
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")

@app.post("/clone")
async def clone(text: str = Form(...)):

    tts.tts_to_file(
        text=text,
        file_path="output.wav"
    )

    return FileResponse("output.wav")
