from transformers import pipeline
import whisper

accent_classifier = pipeline("audio-classification", model="dima806/english_accents_classification")
whisper_model = whisper.load_model("base")

def classify_accent(audio_path):
    results = accent_classifier(audio_path)
    return results[0]["label"], results[0]["score"] * 100

def transcribe_audio(audio_path):
    result = whisper_model.transcribe(audio_path)
    return result["language"], result["text"]
