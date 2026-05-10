from email.mime import text
from unicodedata import category

from app.utils.category_utils import calculate_category_score
from app.utils.priority_utils import calculate_priority, calculate_confidence
from app.services.image_ai import get_image_description


class AiService:

    def analyze(self, request):

        text = request.description.lower()

        image_text = ""
        if request.imageUrl:
            image_text = get_image_description(request.imageUrl).lower()

        full_text = f"{image_text}"

        print("Full text for analysis:", full_text)

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
            f"AI vision: {image_text}."
        )[:250]

        return {
            "category": category,
            "summary": summary,
            "priority": priority,
            "confidence": confidence,
            "categoryMatch": match
        }