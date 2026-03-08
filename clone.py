from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from TTS.api import TTS

app = FastAPI()

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

@app.post("/clone")
async def clone(voice: UploadFile, text: str = Form(...)):

    with open("voice.wav","wb") as f:
        f.write(await voice.read())

    tts.tts_to_file(
        text=text,
        speaker_wav="voice.wav",
        language="pt",
        file_path="output.wav"
    )

    return FileResponse("output.wav")
