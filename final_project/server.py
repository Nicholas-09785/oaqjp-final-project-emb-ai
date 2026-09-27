"""Flask server for emotion detection."""

from flask import Flask, request

from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze submitted text and return its emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
