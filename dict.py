# French Dictionary
with open('dictionnaire_francais.txt', 'r') as f:
    dict_french = [line.strip() for line in f]

# English Dictionary
with open('dictionnaire_anglais.txt', 'r') as f:
    dict_english = [line.strip() for line in f]

if __name__ == '__main__':
    print(dict_french[1:5])
    print(dict_english[1:5])