import json
import requests


def emotion_detector(text_to_analyze):
    url = (
        'https://sn-watson-emotion.labs.skills.network'
        '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    dict_to_send = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=dict_to_send, headers=headers, timeout=10)

    if response.status_code == 200:
        formatted_output = json.loads(response.text)
        emotions = formatted_output['emotionPredictions'][0]["emotion"]
        result = {**emotions, 'dominant_emotion': max(emotions, key=emotions.get)}
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

