import streamlit as st
from utils.audio_utils import download_video, extract_audio
from utils.model_utils import classify_accent, transcribe_audio
import os

st.title("English Accent Detector")
st.write("Upload or paste a video URL to detect the speaker's English accent.")

video_url = st.text_input("Enter public video URL (MP4 or Loom):")

if st.button("Analyze") and video_url:
    try:
        with st.spinner("Downloading video and extracting audio..."):
            video_path = download_video(video_url)
            audio_path = extract_audio(video_path)

        with st.spinner("Running accent classification..."):
            accent, confidence = classify_accent(audio_path)
            st.write(f"**Predicted Accent:** {accent}")
            st.write(f"**Confidence:** {confidence:.2f}%")

        with st.spinner("Running Whisper transcription..."):
            language, transcript = transcribe_audio(audio_path)
            st.write(f"**Language Detected:** {language}")
            st.text_area("Transcript Preview", transcript[:300])

    except Exception as e:
        st.error(f"Error: {str(e)}")

    finally:
        # Cleanup files
        for f in [video_path, audio_path]:
            if os.path.exists(f):
                os.remove(f)
# force rebuild