#!/usr/bin/env python3

import json
import csv
import os
import sys

from os import listdir
from os.path import isfile, join,abspath
from jinja2 import Template


input_path = sys.argv[1]
output_html=sys.argv[2]

template_fraction = """

        <div class="row center">
   <table id="ffufreport">
        <thead>
          <tr>
              <th>Status</th>
              <th>FUZZ</th>
              <th>URL</th>
              <th>Redirect location</th>
              <th>Position</th>
              <th>Length</th>
              <th>Words</th>
              <th>Lines</th>
          </tr>
        </thead>
        <tbody>
    {% for result in results %}
                <tr class="result-{{ result["status_code"] }}" style="background-color: {{result["HTMLColor"]}};">
                <td><font color="black" class="status-code">{{ result["status_code"] }}</font></td>
                <td>{{ result["FUZZ"] }}</td>
                <td><a href="{{ result["url"] }}">{{ result["url"] }}</a></td>
                <td>{{ result["redirectlocation"] }}</td>
                <td>{{ result["position"] }}</td>
                <td>{{ result["content_length"] }}</td>
                <td>{{ result["content_words"] }}</td>
                <td>{{ result['content_lines'] }}</td>
                </tr>
            {% endfor %}
        </tbody>
      </table>
  </div>
<br /><br />
<br /><br />
<br /><br />

"""

def colorizeResults(results):
    for result in results:
        s = result.status_code
        if s >= 200 and s <= 299:
            result["HTMLColor"] = "#adea9e"
            continue
        if s >= 300 and s <= 399:
            result["HTMLColor"] = "#bbbbe6"
            continue
        if s >= 400 and s <= 499:
            result["HTMLColor"] = "#d2cb7e"
            continue
        if s >= 500 and s <= 599:
            result["HTMLColor"] = "#de8dc1"
            continue


def read_csv(input):
    results = [dict(d) for d in csv.DictReader(open(input))]
    print("results          "   )
    print('[%s]' % ', '.join(map(str, results)))
    return results

def get_files_list(dir):
    for dirpath, _, filenames in os.walk(dir):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

def write_martrix(matrix,output):
    template = Template(template_fraction)

    for results in matrix:
        output.write(template.render(results=results))


def main():

    files = get_files_list(input_path)
    matrix = [ read_csv(file) for file in files]

    print("matrix             " )
    print('[%s]' % ', '.join(map(str, matrix)))

    output = open(output_html,'a')
    write_martrix(matrix, output)

    output.close()


if __name__ == '__main__':
    main()
