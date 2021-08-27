from googletrans import Translator
import re

translator = Translator(service_urls=['translate.googleapis.com'])
translator = Translator()

file = "/home/levi/dev-ops/python-translation/quest-test.txt"
file1 = "/home/levi/dev-ops/python-translation/quest-test-translated.txt"
# file1 = file+".copy"

with open(file, "r") as f:
    # for i = 0 len(f.readlines()) i++:
    for i in f:
        # line = f.readline()
        line = i
        m = re.search(r'".*"', line)
        # i = re.search(r'(\s+)(\w|\d)', line)
        if m:
            # print(len(i.group(0)))
            # print(m.text)
            to_translate = m.group(0)
            translated = translator.translate(to_translate, dest='en')
            with open(file1, "a") as f1:
                f1.write(line[:m.start()]+str(translated.text)+line[m.end():])
                f1.close()
        else:
            with open(file1, "a") as f1:
                f1.write(line)
                f1.close()
f.close()
