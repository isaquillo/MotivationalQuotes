import requests
import deepl

quote_api_url = 'https://zenquotes.io/api/random'

def getQuote():
    try:
        response = requests.get(quote_api_url)
        data = response.json()[0]
        quote = data['q']
        author = data['a']
        return quote, author, None
    except Exception as e:
        return False, None, e
    


def translate_quote(quote):
    try:
        auth_key = "b8b62f0b-9fab-23ca-377a-730a1895b6e8:fx"
        translator = deepl.Translator(auth_key)
        result = translator.translate_text(quote, target_lang="ES")
        return result.text, None
    except Exception as e:
        return False, e
    