import os
import requests


def get_voice(filename):
    subscription_key = os.environ['SPEECH_KEY']
    region = os.environ['SPEECH_REGION']

    url = "https://{}.tts.speech.microsoft.com/cognitiveservices/v1".format(region)
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-48khz-192kbitrate-mono-mp3"
    }

    with open("./support/pitch.ssml") as file:
        ssml = file.readlines()

    ssml = " ".join(ssml)
    ssml = ssml.encode('utf-8')

    response = requests.post(url=url, data=ssml, headers=headers)

    with open("{}.mp3".format(filename), "wb") as f:
        f.write(response.content)