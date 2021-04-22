from pygoogletranslation import Translator
import webvtt
import os
nazwa_katalogu = "D:\Dropbox\Agusi\Coursera\CNN\Tydzień 1"
nazwa_pliku = list(filter(lambda x: x.endswith('.vtt'), os.listdir(nazwa_katalogu)))
nazwa_pliku = [s for s in nazwa_pliku if "(pl)" not in s]
def create_translate(nazwa_katalogu,nazwa_pliku):
    vtt = webvtt.read(f'{nazwa_katalogu}\{nazwa_pliku}')

    translator = Translator()


    list_sentence = []

    for element_in_vtt in vtt:
        list_sentence.append(element_in_vtt.text)

    translated_lines = []
    for line in list_sentence:
        new_line = line
        split_lines = line.split('.')
        for s_line in split_lines:
            if len(s_line) < 1:
                continue
            trans = translator.translate(s_line, src='en', dest='pl')
            print(f'{trans.origin} -> {trans.text}')
            new_line = new_line.replace(s_line.strip(),trans.text.replace('.',''))
        translated_lines.append(new_line)


    for index,minute in enumerate(vtt):
        minute.text = translated_lines[index]
        vtt[index].text = minute.text

    print(vtt)

    nazwa_pliku = nazwa_pliku.split("(",maxsplit=1)[0]

    vtt.save(f'{nazwa_katalogu}\{nazwa_pliku}(pl)')

for plik in nazwa_pliku:
    create_translate(nazwa_katalogu,"W7 - Jedna warstwa sieci splotowej (ang).vtt")
