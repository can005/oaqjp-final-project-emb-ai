''' Tools available to detect emotions using Watson AI
'''
import json
import requests
def emotion_detector(text_to_analyze):
    URL = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    to_send = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json=to_send,headers=headers, timeout=10)
    formatted_output = json.loads(response.text)
    emotions = formatted_output['emotionPredictions'][0]["emotion"]
    result = {**emotions, 'dominant_emotion': max(emotions, key=emotions.get)}
    return result  
