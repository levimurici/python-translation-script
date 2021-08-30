from googletrans import Translator
import argparse
import re

translator = Translator(service_urls=['translate.googleapis.com'])
translator = Translator()

parser = argparse.ArgumentParser(description='Traduzir substrings de idiomas em encoding UTF-8')


parser.add_argument('-p', '--path', type=str, help='Caminho do arquivo a ser traduzido')
parser.add_argument('-o', '--output', default=f'.translated', type=str, help='Output do arquivo traduzido')
parser.add_argument('-i', '--origin', default='ro', type=str, help='Idioma de origem (default=romanian)')
parser.add_argument('-l', '--language', default='en',type=str, help='Idioma de destino (default=english)')
args = parser.parse_args()

file1 = args.path
file2 = args.output
language = args.language
origin = args.origin

if __name__ == '__main__':  
    with open(file1, "r") as f:
        # for i = 0 len(f.readlines()) i++:
        for i in f:
            # line = f.readline()
            line = i
            m = re.search(r'".*"', line)
            # i = re.search(r'(\s+)(\w|\d)', line)
            if m:
                to_translate = m.group(0)
                translated = translator.translate(to_translate, src=origin, dest=language)
                print(f"{to_translate} >> {translated.text}")
                with open(file2, "a") as f2:
                    f2.write(line[:m.start()]+str(translated.text)+line[m.end():])
                    f2.close()
            else:
                with open(file2, "a") as f2:
                    f2.write(line)
                    f2.close()
    f.close()
