import requests
import googletrans


async def translate_advice():
    url = "https://api.adviceslip.com/advice"
    r = requests.get(url)
    advice = r.json()['slip']['advice']
    print(advice)

    translator = googletrans.Translator()
    tarjima = await translator.translate(advice, dest='uz')

    dict_to_return = {
        "eng": advice,
        "uzb": tarjima.text,
    }

    return dict_to_return

