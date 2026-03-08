from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from TTS.api import TTS
import uuid

app = FastAPI()

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

@app.post("/clone")
async def clone_voice(voice: UploadFile = File(...), text: str = Form(...)):

    voice_path = f"voice_{uuid.uuid4()}.wav"
    output_path = f"output_{uuid.uuid4()}.wav"

    with open(voice_path, "wb") as f:
        f.write(await voice.read())

    tts.tts_to_file(
        text=text,
        speaker_wav=voice_path,
        file_path=output_path
    )

    return FileResponse(output_path)
