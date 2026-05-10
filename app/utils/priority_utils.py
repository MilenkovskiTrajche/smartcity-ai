PRIORITY_KEYWORDS = {
    "CRITICAL": ["fire", "smoke", "explosion", "danger"],
    "HIGH": ["leak", "flood", "broken", "blocked", "crack"],
    "MEDIUM": ["trash", "dirty", "damaged"],
}


def calculate_priority(text: str):
    for level, keywords in PRIORITY_KEYWORDS.items():
        if any(word in text for word in keywords):
            return level

    return "LOW"


def calculate_confidence(scores, best):
    total = sum(scores.values())
    if total == 0:
        return 0.4
    return round(scores[best] / total, 2)