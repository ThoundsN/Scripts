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
fw = open(output_path,'w',encoding='utf-8')

lines =  fr.readlines()
for line in lines:
    link = location2href(line)

    fw.write('<a href="{} "> {} </a>'.format(link,link))
    fw.write('\n')


fw.close()
fr.close()