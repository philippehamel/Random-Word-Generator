from random import randint
from dict import dict_english, dict_french

def random_word(language = 'fr'):
    if language == 'fr':
        return dict_french[randint(0, len(dict_french))]
    if language == 'en':
        return dict_english[randint(0, len(dict_english))]

if __name__ == '__main__':
    print(random_word())