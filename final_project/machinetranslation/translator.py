"""Translator App"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def english_to_french(english_text):
    """Translates english to french"""
    try:
        french_text_request = translator.translate(text=english_text, source='en', target='fr')
        french_text_result = french_text_request.get_result()

        if french_text_request.status_code == 200:
            french_translations = french_text_result['translations']

            if len(french_translations) > 0:
                french_text = french_translations[0]['translation']
    except:
        return None

    return french_text

def french_to_english(french_text):
    """Translates french to english"""
    try:
        english_text_request = translator.translate(text=french_text, source='fr', target='en')
        english_text_result = english_text_request.get_result()

        if english_text_request.status_code == 200:
            english_translations = english_text_result['translations']

            if len(english_translations) > 0:
                english_text = english_translations[0]['translation']
    except:
        return None

    return english_text

authenticator=IAMAuthenticator(apikey)

translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator.set_service_url(url)
