#!/usr/bin/env python3
from jinja2 import Template
import sys


template_string = """
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, maximum-scale=1.0"
    />
    <title>Waybackurls Report - </title>

  </head>
    <body>
    {% for url in urls %}
    <a href="{{ url}}">{{ url }}</a></td>
    {% endfor %}

  </body>
</html>
"""



if __name__ == '__main__':
    input_file = sys.argv[1]
    output_html = sys.argv[2]

    input = open(input_file,'r')
    urls = excludeFileContent = list(filter(None, input.read().splitlines()))

    template = Template(template_string)

    output = open(output_html,'w')
    output.write(template.render(urls=urls))

    output.close()
    input.close()