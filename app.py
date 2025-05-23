import os
import streamlit as st
from utils.audio_utils import download_audio, extract_audio
from utils.model_utils import classify_accent
from tempfile import NamedTemporaryFile

st.title("English Accent Classifier")
st.write("Upload a YouTube video or public MP4 URL to classify the speaker’s English accent.")

url = st.text_input("Enter video URL (YouTube or MP4):")
run_button = st.button("Analyze")

if run_button and url:
    with st.spinner("Downloading and processing video..."):
        video_path = download_audio(url)
        audio_path = extract_audio(video_path)

    with st.spinner("Classifying accent..."):
        predicted_accent = classify_accent(audio_path)
        st.success(f"**Predicted Accent:** {predicted_accent}")

    # Optional: Remove transcription-related UI if not using it
    # with st.spinner("Running Whisper transcription..."):
    #     language, transcript = transcribe_audio(audio_path)
    #     st.write(f"**Language Detected:** {language}")
    #     st.text_area("Transcript Preview", transcript[:300])
