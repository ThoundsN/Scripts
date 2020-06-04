import json
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

def location2href(location):
    prefix = "http://jsrecon.ragnarokv.site/links/"
    pieces = location.split('/')
    del pieces[6]
    del pieces[0:5]
    # print(pieces)
    suffix = "/".join(pieces)
    href = prefix + suffix
    # print(href)
    return  href

fr = open(input_path,'r',encoding='utf-8')
data = json.load(fr)

# print(type(data))

entropys = set()
newdata = list()

for entry in data:
    entry_entropy_value = entry['Details']['Entropy']
    if entry_entropy_value not in entropys:
        newdata.append(entry)
        entropys.add(entry_entropy_value)

# print(type(newdata))

# print(type(x))

for entry in newdata:
    file_location = entry['File']
    href = location2href(file_location)
    entry['href'] = href

x = json.dumps(newdata)

fw = open(output_path,'w',encoding='utf-8')
fw.write(x)
fw.close()
fr.close()