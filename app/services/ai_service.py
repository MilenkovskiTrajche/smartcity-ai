from app.utils.category_utils import calculate_category_score
from app.utils.priority_utils import calculate_priority, calculate_confidence
from app.services.image_ai import get_image_description


class AiService:

    def analyze(self, request):

        text = request.description.lower()

        image_text = ""
        if request.imageUrl:
            image_text = get_image_description(request.imageUrl).lower()

        full_text = text + " " + image_text

        # category
        category, scores = calculate_category_score(full_text)

        # priority
        priority = calculate_priority(full_text)

        # confidence
        confidence = calculate_confidence(scores, category)

        # institution mapping
        institution_map = {
            "water": "water",
            "fire": "electricity",
            "waste": "sanitation",
            "road": "roads"
        }

        institution = institution_map.get(category, "general")

        match = request.category.lower() == category if request.category else True

        summary = f"{text} | image: {image_text}"[:200]

        return {
            "category": category,
            "summary": summary,
            "priority": priority,
            "institutionCategory": institution,
            "confidence": confidence,
            "categoryMatch": match
        }