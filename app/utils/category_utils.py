CATEGORY_KEYWORDS = {
    "water": ["water", "leak", "flood", "pipe", "burst"],
    "fire": ["fire", "smoke", "burning", "flames"],
    "waste": ["trash", "garbage", "waste", "dump"],
    "road": ["road", "crack", "pothole", "asphalt", "damage"]
}


def calculate_category_score(text: str):
    scores = {}

    for category, keywords in CATEGORY_KEYWORDS.items():
        score = sum(1 for word in keywords if word in text)
        scores[category] = score

    best = max(scores, key=scores.get)
    return best, scores