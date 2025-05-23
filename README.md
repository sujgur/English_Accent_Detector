# 🗣️ English Accent Detection App

This Streamlit application detects English accents from public video URLs using a Hugging Face model. It extracts audio from a video, processes the audio, and classifies the speaker's accent.

## 🚀 Demo

[![Open in Spaces](https://img.shields.io/badge/-Open%20in%20Hugging%20Face%20Spaces-blue?logo=HuggingFace)](https://huggingface.co/spaces/YOUR_USERNAME/YOUR_REPO_NAME)

## 🔍 Model

We use [`dima806/english_accents_classification`](https://huggingface.co/dima806/english_accents_classification), a fine-tuned model for classifying English accents such as:
- American
- British
- Indian
- Australian
- Canadian

## 🧠 Features

- 🎞️ Accepts public video URLs
- 🔊 Extracts audio using `moviepy`
- 🧠 Predicts accent using a Hugging Face model
- 🖼️ Interactive web UI built with Streamlit

## 📦 Requirements

The app uses the following Python libraries:
- `streamlit`
- `transformers`
- `torch`
- `moviepy`
- `whisper`
- `pydub`

These are listed in `requirements.txt`.

## 🐍 Python Version

Ensure you use **Python 3.10** for compatibility with `tokenizers` and `PyO3`.

```text
runtime.txt:
python-3.10.13
