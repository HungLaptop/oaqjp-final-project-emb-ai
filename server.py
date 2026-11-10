from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/emotionDetector")
def analyze_emotion():
    text = request.args.get("textToAnalyze", "").strip()
    if not text:
        return "Please enter some text to analyze."

    result = emotion_detector(text)
    scores = ", ".join(
        f"{emotion}: {result[emotion]:.4f}"
        for emotion in ("anger", "disgust", "fear", "joy", "sadness")
    )
    return f"{scores}. Dominant emotion: {result['dominant_emotion']}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)