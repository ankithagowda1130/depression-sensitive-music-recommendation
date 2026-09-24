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

emotion_words = {
    "happy": [
        "happy", "joy", "excited", "great", "good",
        "wonderful", "awesome", "love", "fun"
    ],
    "sad": [
        "sad", "upset", "lonely", "cry", "unhappy",
        "hurt", "low", "depressed", "down"
    ],
    "angry": [
        "angry", "mad", "frustrated", "annoyed",
        "irritated", "furious", "hate"
    ],
    "relaxed": [
        "calm", "relaxed", "peaceful", "chill",
        "comfortable", "quiet"
    ]
}


def detect_emotion(text):
    text = text.lower()
    scores = {}

    for emotion, words in emotion_words.items():
        scores[emotion] = 0

        for word in words:
            if word in text:
                scores[emotion] += 1

    best_emotion = max(scores, key=scores.get)

    if scores[best_emotion] == 0:
        return "neutral"

    return best_emotion


def recommend_music(emotion):
    print("\nDetected Emotion:", emotion.upper())
    print("\nRecommended Songs:")

    for song in music[emotion]:
        print("-", song)


print("====================================")
print("Depression Sensitive Music Recommendation")
print("====================================")

while True:
    user_input = input("\nHow are you feeling? ")

    if user_input.lower() == "exit":
        print("Thank you!")
        break

    emotion = detect_emotion(user_input)
    recommend_music(emotion)
