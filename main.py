import random

music = {
    "happy": [
        "Happy - Pharrell Williams",
        "On Top of the World - Imagine Dragons",
        "Count on Me - Bruno Mars"
    ],
    "sad": [
        "Fix You - Coldplay",
        "Let Her Go - Passenger",
        "Someone You Loved - Lewis Capaldi"
    ],
    "angry": [
        "Believer - Imagine Dragons",
        "Stronger - Kelly Clarkson"
    ],
    "relaxed": [
        "Perfect - Ed Sheeran",
        "Photograph - Ed Sheeran"
    ],
    "neutral": [
        "Golden Hour - JVKE",
        "Dandelions - Ruth B."
    ]
}


def detect_emotion(text):
    text = text.lower()

    happy_words = ["happy", "good", "great", "excited", "joy", "awesome", "love"]
    sad_words = ["sad", "lonely", "cry", "upset", "hurt", "unhappy", "low"]
    angry_words = ["angry", "mad", "frustrated", "annoyed", "hate"]
    relaxed_words = ["calm", "relaxed", "peaceful", "quiet", "chill"]

    scores = {
        "happy": 0,
        "sad": 0,
        "angry": 0,
        "relaxed": 0
    }

    for word in happy_words:
        if word in text:
            scores["happy"] += 1

    for word in sad_words:
        if word in text:
            scores["sad"] += 1

    for word in angry_words:
        if word in text:
            scores["angry"] += 1

    for word in relaxed_words:
        if word in text:
            scores["relaxed"] += 1

    if max(scores.values()) == 0:
        return "neutral"

    return max(scores, key=scores.get)


def recommend_music(text):
    emotion = detect_emotion(text)

    print("\nDetected Emotion:", emotion.upper())
    print("\nRecommended Songs:")

    for song in music[emotion]:
        print("-", song)


print("====================================")
print("Depression Sensitive Music Recommendation")
print("====================================")

user_input = input("\nHow are you feeling? ")

recommend_music(user_input)
