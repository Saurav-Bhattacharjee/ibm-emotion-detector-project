import requests
import json

def emotion_detector(text_to_analyze):
    #Function to analyse the text 
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload={ "raw_document": { "text": text_to_analyze } } 
    response = requests.post(url, json=payload, headers=headers)
    data=json.loads(response.text)
    all_emotion=data['emotionPredictions'][0]['emotion']
    dominant = max(all_emotion,key=all_emotion.get)
    all_emotion['dominant_emotion']= dominant
    return all_emotion

     
