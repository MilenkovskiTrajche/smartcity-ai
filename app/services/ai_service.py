from email.mime import text
from unicodedata import category

from httpcore import request

from app.utils.category_utils import calculate_category_score
from app.utils.priority_utils import calculate_priority, calculate_confidence
from app.services.image_ai import get_image_description


class AiService:

    def analyze(self, request):

        text = request.description.lower()
        image_text = ""

        if request.imageUrl and request.imageUrl.strip():

            image_text = get_image_description(
                request.imageUrl
            ).lower()

        else:
            print("No image URL provided.")

        full_text = f"{text} {image_text}".strip()
        # category
        category, scores = calculate_category_score(full_text)

        # priority
        priority = calculate_priority(full_text)

        # confidence
        confidence = calculate_confidence(scores, category)

        match = request.category.lower() == category if request.category else True

        summary = (
            f"Issue detected: {category}. "
            f"User report: {text}. "
            f"AI vision: {image_text if image_text else 'not available'}"
        )[:250]

        return {
            "category": category,
            "summary": summary,
            "priority": priority,
            "confidence": confidence,
            "categoryMatch": match
        }

    def generate_description(self, request):
        
        image_text = ""

        if request.imageUrl and request.imageUrl.strip():

            image_text = get_image_description(
                request.imageUrl
            ).lower()
        else:
            print("No image URL provided.")

        full_text = f"{image_text}".strip()
        
        return {
            "description": full_text
        } 
