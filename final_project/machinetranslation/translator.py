#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator1 = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-09-11',
    authenticator=authenticator1
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    french_text_res = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_text_res

def french_to_english(french_text):
    english_text_res = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text_res
