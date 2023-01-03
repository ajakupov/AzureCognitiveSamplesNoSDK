import os
import requests
import json
import uuid

def translate_text(text):
    resource_key = os.environ['TRANSLATOR_TEXT_RESOURCE_KEY']
    region = os.environ['TRANSLATOR_TEXT_REGION']
    endpoint = os.environ['TRANSLATOR_TEXT_ENDPOINT']

    path = '/translate'
    params = {
        'api-version': '3.0',
        'from': 'ru',
        'to': 'kk'
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': resource_key,
        'Ocp-Apim-Subscription-Region': region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]
    request = requests.post(constructed_url, headers=headers, json=body, params=params)
    response = request.json()

    return response[0]['translations'][0]['text']
