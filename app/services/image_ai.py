import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import requests
from io import BytesIO
torch.set_num_threads(1)  # Limit to 1 thread for better performance in web server context

model = None
processor = None
tokenizer = None

def load_model():
    global model, processor, tokenizer

    if model is None:
        model = VisionEncoderDecoderModel.from_pretrained(
            "nlpconnect/vit-gpt2-image-captioning"
        )
        processor = ViTImageProcessor.from_pretrained(
            "nlpconnect/vit-gpt2-image-captioning"
        )
        tokenizer = AutoTokenizer.from_pretrained(
            "nlpconnect/vit-gpt2-image-captioning"
        )


def get_image_description(image_url: str) -> str:
    try:
        load_model()

        image = Image.open(BytesIO(requests.get(image_url).content)).convert("RGB")

        pixel_values = processor(images=image, return_tensors="pt").pixel_values

        with torch.no_grad():
            output_ids = model.generate(pixel_values)

        caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        return caption

    except Exception as e:
        print("IMAGE AI ERROR:", str(e))
        return "unknown image"