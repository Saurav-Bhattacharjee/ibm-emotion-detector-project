"""Flask server for emotion detection application."""
from flask import Flask,request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route('/emotionDetector')
def emo_detector():
    """Handles emotion detection request and returns formatted response."""
    text_to_analyze= request.args.get('textToAnalyze')
    result= emotion_detector(text_to_analyze)
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']

    if dominant is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}.")

@app.route("/")
def render_index_page():
    """Renders the home page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
