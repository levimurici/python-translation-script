from googletrans import Translator
import re

sentence = []

translator = Translator(service_urls=['translate.googleapis.com'])
translator = Translator()

f = open("/home/levi/dev-ops/python-translation/quest-test.txt", "r")
print("Nome: ",f.name)

for x in f:
    line = f.readline()
    m = re.search(r'".*"', line)
    if m:
        print(m.group(0))
        to_translate = m.group(0)
        translated = translator.translate(to_translate, dest='en')
        sentence.append(translated.text)

print(sentence)
f.close()
