CATEGORY_KEYWORDS = {
    "water": [
        "leak", "flood", "burst pipe", "water overflow", "sewage", "drainage"
    ],

    "fire": [
        "fire", "smoke", "burning", "flames", "explosion"
    ],

    "road": [
        "pothole", "crack", "asphalt damage", "road collapse", "uneven road", "bridge damage"
    ],

    "traffic": [
        "accident", "car crash", "collision", "traffic jam", "blocked road"
    ],

    "waste": [
        "garbage", "trash", "litter", "dumping", "overflow bin"
    ],

    "electricity": [
        "power outage", "electricity cut", "spark", "broken wire", "broken streetlight"
    ],

    "public_safety": [
        "danger", "hazard", "unsafe", "exposed wires", "assault", "theft"
    ]
}


def calculate_category_score(text: str):
    text = text.lower()

    scores = {c: 0 for c in CATEGORY_KEYWORDS}

    for category, keywords in CATEGORY_KEYWORDS.items():
        for word in keywords:
            if word in text:
                weight = len(word.split())
                scores[category] += weight


    if "road" in text and "accident" in text:
        scores["traffic"] += 3

    if "leak" in text and "road" in text:
        scores["road"] += 3
        scores["water"] += 1

    if "construction" in text:
        scores["infrastructure"] += 2

    best = max(scores, key=scores.get)

    return best, scores