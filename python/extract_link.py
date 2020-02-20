import gc
import sys
import re
from bs4 import BeautifulSoup

input_path = sys.argv[1]
output_path1 = sys.argv[2]
output_path2 = sys.argv[3]

specific_words = "admin,test,dev,beta,internal,prod,wss://,websocket,ws://,wsdl,firebase"

specific_words = re.split(',', specific_words)

api_wordlist = "api v1 v2 v3 v4 v5 v6"

api_wordlist = re.split(' ', api_wordlist)



def write(input,output,wordlist):
    fp = open(input, 'r', encoding="utf-8")
    soup = BeautifulSoup(fp, "html.parser")
    for div in soup.body.find_all('div', recursive=False):
        # print(div.a.text)
        hasword = False
        # print('\n')
        # print('\n')
        for word in wordlist:
            if word in str(div.a.text):
                hasword = True
                break
        if not hasword:
            div.decompose()

            # except Exception as e:
            #     print(e)
            #     print(div)

    fw1 = open(output, 'w', encoding="utf-8")
    fw1.write(soup.prettify())
    fw1.close()
    fp.close()

    soup.decompose()
    gc.collect()


if __name__ == '__main__':

    write(input_path,output_path1,specific_words)
    write(input_path,output_path2,api_wordlist)

