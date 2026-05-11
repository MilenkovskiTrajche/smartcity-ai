from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
from io import BytesIO

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def get_image_description(image_url: str) -> str:
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content)).convert("RGB")

        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)

        caption = processor.decode(out[0], skip_special_tokens=True)

        return caption

    except Exception as e:
        return "unknown image"