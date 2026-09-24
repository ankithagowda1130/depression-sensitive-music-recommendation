import csv
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


def load_dataset():
    data = []

    with open("dataset.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data


def detect_emotion(text, dataset):
    text = text.lower()

    best_emotion = "neutral"
    best_score = 0

    for row in dataset:
        words = row["text"].lower().split()
        score = 0

        for word in words:
            word = word.strip(".,!?")

            if len(word) > 2 and word in text:
                score += 1

        if score > best_score:
            best_score = score
            best_emotion = row["emotion"]

    return best_emotion


def recommend_music(emotion):
    print("\nDetected Emotion:", emotion.upper())
    print("\nRecommended Songs:")

    songs = music[emotion]

    for song in random.sample(songs, len(songs)):
        print("-", song)


print("====================================")
print("Depression Sensitive Music Recommendation")
print("====================================")

dataset = load_dataset()

user_input = input("\nHow are you feeling? ")

emotion = detect_emotion(user_input, dataset)

recommend_music(emotion)
