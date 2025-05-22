from transformers import pipeline
import whisper
import streamlit as st

@st.cache_resource(show_spinner=False)
def load_accent_classifier():
    return pipeline("audio-classification", model="dima806/english_accents_classification")

@st.cache_resource(show_spinner=False)
def load_whisper_model():
    return whisper.load_model("base")

accent_classifier = load_accent_classifier()
whisper_model = load_whisper_model()

def classify_accent(audio_path):
    results = accent_classifier(audio_path)
    return results[0]["label"], results[0]["score"] * 100

def transcribe_audio(audio_path):
    result = whisper_model.transcribe(audio_path)
    return result["language"], result["text"]
