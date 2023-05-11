from ninja.files import UploadedFile
import replicate
from core.models import SpeechModel

def speech2text_serivce(us_file: str, uploaded_file: UploadedFile):
    output = replicate.run(
        "openai/whisper:e39e354773466b955265e969568deb7da217804d8e771ea8c9cd0cef6591f8bc",
        input={"audio": open(us_file, "rb")},
    )
    SpeechModel.objects.create(
        transcription=output["transcription"],
        segments=output["segments"],
        audio_file=uploaded_file
    )
    return {"text": output}
