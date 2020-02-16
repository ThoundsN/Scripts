import json
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

fr = open(input_path,'r',encoding='utf-8')
data = json.load(fr)

print(type(data))

entropys = set()
newdata = list()

for entry in data:
    entry_entropy_value = entry['Details']['Entropy']
    if entry_entropy_value not in entropys:
        newdata.append(entry)
        entropys.add(entry_entropy_value)

# print(type(newdata))

x = json.dumps(newdata)
# print(type(x))

fw = open(output_path,'w',encoding='utf-8')
fw.write(x)
fw.close()
fr.close()