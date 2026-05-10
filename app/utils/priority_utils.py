PRIORITY_KEYWORDS = {
    "CRITICAL": ["fire", "smoke", "explosion", "danger"],
    "HIGH": ["leak", "flood", "broken", "blocked", "crack"],
    "MEDIUM": ["trash", "dirty", "damaged"],
}


def calculate_priority(text: str):
    text = text.lower()

    # CRITICAL safety risks
    if any(w in text for w in ["fire", "explosion", "gas leak", "electric shock"]):
        return "CRITICAL"

    # HIGH public disruption
    if any(w in text for w in ["accident", "flood", "collapse", "blocked", "leak"]):
        return "HIGH"

    # MEDIUM damage
    if any(w in text for w in ["pothole", "trash", "broken", "damage"]):
        return "MEDIUM"

    return "LOW"


def calculate_confidence(scores, best):
    total = sum(scores.values())

    if total == 0:
        return 0.35

    best_score = scores[best]
    confidence = best_score / (total + 0.0001)

    # normalize slightly
    return round(min(0.95, max(0.4, confidence)), 2)