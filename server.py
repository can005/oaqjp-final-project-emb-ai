''' Executing this function initiates the application of emotional
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def run_emotion_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detector()
        function. The output returned shows the emotions and its scores
        alongside the dominant emotion
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    output = emotion_detector(text_to_analyze)

    if output['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {output['anger']}, 'disgust': {output['disgust']}, "
        f"'fear': {output['fear']}, 'joy': {output['joy']}, "
        f"'sadness': {output['sadness']}. "
        f"The dominant emotion is {output['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
