from faster_whisper import WhisperModel


model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(state):

    audio_path = state["file_path"]

    segments, info = model.transcribe(audio_path)

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "
    
    transcript = transcript.strip()

    state["contents"]["audio"].append(
    {
        "text": transcript,
        "duration": info.duration,
        # "audio_format": info.audio_format,
    }
    )

    return state

if __name__ == "__main__":

    state = {
        "file_path": "sample_data/sample_audio.mp4",
        "contents": {
            "pdf": [],
            "image": [],
            "audio": []
        }
    }

    result = transcribe_audio(state)

    print(result)