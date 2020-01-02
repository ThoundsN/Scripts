#!/usr/bin/env python3

import json
import csv
import sys

from os import listdir
from os.path import isfile, join
from jinja2 import Template


input_path = sys.argv[1]
output_html=sys.argv[2]

template_fraction = """

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
                <tr class="result-{{ result["StatusCode"] }}" style="background-color: {{result["HTMLColor"]}};">
                <td><font color="black" class="status-code">{{ result["StatusCode"] }}</font></td>
                <td>{{ result["keyword"] }}</td>
                <td>{{ result["Url"] }}</td>
                <td>{{ result["RedirectLocation"] }}</td>
                <td>{{ result["Position"] }}</td>
                <td>{{ result["ContentLength"] }}</td>
                <td>{{ result["ContentWords"] }}</td>
                <td>{{ result["ContentLines"] }}</td>
                </tr>
            {% endfor %}
        </tbody>
      </table>
  


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
    results = [json.dumps(d) for d in csv.DictReader(open(input))]
    print("results          "   )
    print('[%s]' % ', '.join(map(str, results)))
    return results

def get_files_list(dir):
    files_list = [f for f in listdir(dir) if isfile(join(dir, f))]
    print("file list             " )
    print('[%s]' % ', '.join(map(str, files_list)))

    return files_list

def write_martrix(matrix,output):
    template = Template(template_fraction)

    for results in matrix:
        output.write(template.render(results=results))


def main():

    files = get_files_list(input_path)
    matrix = [ read_csv(file) for file in files]

    print("matrix             " )
    print('[%s]' % ', '.join(map(str, matrix)))

    output = open(output_html,'w')
    write_martrix(matrix, output)

    output.close()


if __name__ == '__main__':
    main()
