# 🧠 SmartCity AI Service (Python)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-orange?style=for-the-badge)](https://huggingface.co/Salesforce/blip-image-captioning-base)

A lightweight AI-powered microservice built with **FastAPI** that automates the analysis of urban incident reports. By combining traditional keyword scoring with Deep Learning vision models, it accurately classifies city issues and determines response priority.

---

## 🚀 Features

- **Hybrid Intelligence:** Fuses text-based keyword analysis with AI image captioning.
- **Computer Vision:** Uses the **BLIP (Bootstrapping Language-Image Pre-training)** model to interpret incident photos.
- **Smart Classification:** Categorizes issues into Water, Fire, Road, Traffic, Waste, Electrical, or Safety.
- **Urgency Logic:** Automatically assigns priority levels (**LOW** → **CRITICAL**) based on the fused data.
- **Seamless Integration:** Optimized for use as a sidecar service for **Spring Boot** or other backend architectures.
- **Confidence Scoring:** Provides a reliability metric for every classification.

---

## 🏗️ Project Structure

```text
app/
├── main.py                # FastAPI entry point & API routes
├── services/
│   └── image_ai.py        # BLIP model loading & inference logic
└── utils/
    ├── category_utils.py  # Rule-based scoring & category mapping
    └── priority_utils.py  # Severity assessment logic


# Create the environment
python -m venv .venv

# Activate it
# On macOS / Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload --port 8000

Endpoint: POST /analyze