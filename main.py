from fastapi import FastAPI
from twilio.rest import Client
import azure.cognitiveservices.speech as speechsdk
import os

app = FastAPI()

# Twilio Credentials
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"

# Azure Speech API Credentials
AZURE_SPEECH_KEY = "your_azure_speech_key"
AZURE_REGION = "your_azure_region"

# Function to generate AI speech response
def generate_speech(text):
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_REGION)
    file_name = "response.wav"
    audio_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(text).get()
    
    return file_name

# Function to make the call
def make_call(to_number, text):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    audio_file = generate_speech(text)
    
    call = client.calls.create(
        twiml=f'<Response><Play>{audio_file}</Play></Response>',
        to=to_number,
        from_=TWILIO_PHONE_NUMBER
    )
    
    return {"message": "Call initiated!", "call_sid": call.sid}

# API Endpoint
@app.post("/call/")
def call_customer(to_number: str, message: str):
    return make_call(to_number, message)

