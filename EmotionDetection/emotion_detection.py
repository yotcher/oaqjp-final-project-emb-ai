import requests
import json
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    JSON = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json=JSON, headers=headers)
    formatted_response = json.loads(response.text)
    dict_response = formatted_response['emotionPredictions'][0]['emotion']
    max_emotion = max(dict_response, key=lambda x: dict_response[x])
    dict_response['dominant_emotion'] = max_emotion
    return dict_response