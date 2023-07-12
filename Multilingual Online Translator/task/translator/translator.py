import requests
from bs4 import BeautifulSoup
import argparse


parser = argparse.ArgumentParser(description="Enter")
parser.add_argument("source")
parser.add_argument("target")
parser.add_argument("word")
args = parser.parse_args()


def trans(dir, dirto, word):
    file = open(f'{word}.txt', 'w', encoding='utf8')
    dirurl = f'{dir.lower()}-{dirto.lower()}'
    url = f'https://context.reverso.net/translation/{dirurl}/{word}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    words = soup.find_all('span', {'class': 'display-term'})
    if len(words)==0:
        print(f'Sorry, unable to find {word}')
        exit()
    print(f'\n{dirto} Translations:')
    print(f'\n{dirto} Translations:', file=file)
    for i in words:
        print(i.get_text().strip().lower())
        print(i.get_text().strip().lower(), file=file)

    examples_1 = soup.find_all('div', {'class': 'src ltr'})
    examples_2 = soup.find_all('div', {'class': ["trg ltr", "trg rtl arabic", "trg rtl"]})
    exampleslist1 = []
    exampleslist2 = []
    for j in examples_1:
        exampleslist1.append(j.get_text().strip())
    for j in examples_2:
        exampleslist2.append(j.get_text().strip())

    print(f'\n{dirto} Examples:')
    print(f'\n{dirto} Examples:', file=file)
    for i in range(len(examples_1)):
        print(f'{exampleslist1[i]}\n{exampleslist2[i]}\n')
        print(f'{exampleslist1[i]}\n{exampleslist2[i]}\n', file=file)
    file.close()


def transall(dir, word):
    file = open(f'{word}.txt', 'w', encoding='utf8')
    for lang in langlist[1:]:
        if lang.lower() != dir.lower():
            dirto = lang
            dirurl = f'{dir.lower()}-{dirto.lower()}'
            url = f'https://context.reverso.net/translation/{dirurl}/{word}'
            headers = {'User-Agent': 'Mozilla/5.0'}
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            words = soup.find_all('span', {'class': 'display-term'})
            if len(words) == 0:
                print(f'Sorry, unable to find {word}')
                exit()
            print(f'\n{dirto} Translations:')
            print(f'\n{dirto} Translations:', file=file)
            print(words[0].get_text().strip().lower())
            print(words[0].get_text().strip().lower(), file=file)

            examples_1 = soup.find_all('div', {'class': 'src ltr'})
            examples_2 = soup.find_all('div', {'class': ["trg ltr", "trg rtl arabic", "trg rtl"]})
            e1=examples_1[0].get_text().strip()
            e2=examples_2[0].get_text().strip()

            print(f'\n{dirto} Examples:')
            print(f'\n{dirto} Examples:', file=file)
            print(f'{e1}\n{e2}\n')
            print(f'{e1}\n{e2}\n', file=file)

    file.close()


inp = ['english', 'all', 'brrrrrrrrrrrrrrrrk']
langlist = ['all', 'Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']
langlistlow = ['all', 'arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish']
msg = 'Hello, welcome to the translator. Translator supports:\n1. Arabic\n2. German\n3. English\n4. Spanish\n5. French\n6. Hebrew\n7. Japanese\n8. Dutch\n9. Polish\n10. Portuguese\n11. Romanian\n12. Russian\n13. Turkish'
'''
print(msg)
dire = langlist[int(input('Type the number of your language:'))]
direto = langlist[int(input("Type the number of a language you want to translate to or '0' to translate to all languages:"))]
worde = input('Type the word you want to translate:')
print("200 OK")

dire = inp[0]
direto = inp[1]
worde = inp[2]
'''
dire = args.source
direto = args.target
worde = args.word

if dire not in langlistlow:
    print(f"Sorry, the program doesn't support {dire}")
elif direto not in langlistlow:
    print(f"Sorry, the program doesn't support {direto}")
elif 200 != 200:
    print('Something wrong with your internet connection')
elif direto != 'all':
    trans(dire, direto, worde)
else:
    transall(dire, worde)
