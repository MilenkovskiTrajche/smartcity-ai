FROM python:3.11-slim

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# HuggingFace cache location
ENV HF_HOME=/app/hf_cache
ENV TRANSFORMERS_CACHE=/app/hf_cache

RUN mkdir -p /app/hf_cache

COPY requirements.txt .

# install torch CPU version
RUN pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu

# install remaining packages
RUN pip install --no-cache-dir -r requirements.txt

# 🔥 PRE-DOWNLOAD MODEL DURING BUILD
RUN python -c "\
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer; \
VisionEncoderDecoderModel.from_pretrained('nlpconnect/vit-gpt2-image-captioning'); \
ViTImageProcessor.from_pretrained('nlpconnect/vit-gpt2-image-captioning'); \
AutoTokenizer.from_pretrained('nlpconnect/vit-gpt2-image-captioning')"

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
