import gc
import sys
import re
from bs4 import BeautifulSoup

input_path = sys.argv[1]
output_path1 = sys.argv[2]
output_path2 = sys.argv[3]

specific_words = "admin,test,dev,beta,internal,prod"

specific_words = re.split(',', specific_words)

api_wordlist = "api v1 v2 v3 v4 v5 v6"

api_wordlist = re.split(' ', api_wordlist)

if __name__ == '__main__':
    fp = open(input_path, 'r', encoding="utf-8")
    soup1 = BeautifulSoup(fp, "html.parser")
    for div in soup1.body.find_all('div', recursive=False):
        # print(div)
        for word in specific_words:
            try:
                if word not in str(div.a.string):
                    div.decompose()
            except Exception as e:
                print(e)
                continue
    fw1 = open(output_path1, 'w', encoding="utf-8")
    fw1.write(soup1.prettify())
    fw1.close()
    fp.close()

    soup1.decompose()
    gc.collect()

    fp = open(input_path, 'r', encoding="utf-8")
    soup2 = BeautifulSoup(fp, "html.parser")
    for div in soup2.body.find_all('div', recursive=False):
        # print(div)
        for word in api_wordlist:
            try:
                if word not in str(div.a.string):
                    div.decompose()
            except Exception as e :
                print(e)
                continue
    fw2 = open(output_path2, 'w', encoding="utf-8")
    fw2.write(soup2.prettify())
    fw2.close()
    fp.close()
