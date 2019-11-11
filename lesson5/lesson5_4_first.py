#!/usr/bin/python3

import requests

def translate_yandex(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20160119T035517Z.50c6906978ef1961.08d0c5ada49017ed764c042723895ffab867be7a'
    text = text
    lang = 'en-ru'
    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
    return r.text[r.text.find('['):-1].strip("[]\"")


with open("lesson5_4_rus.txt", "w") as lesson5_4_rus:
    with open("lesson5_4_en.txt") as lesson5_4_en:
        for line in lesson5_4_en:
            string = line.split()
            string[0] = translate_yandex(string[0])    
            print(" ".join(string), file = lesson5_4_rus) 

