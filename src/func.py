import requests


def load_random_word():
    """
    getting words form json storage,
    :return: a.m. OBJECT
    """

    response = requests.get('https://www.jsonkeeper.com/b/7L3S')
    words = response.json()