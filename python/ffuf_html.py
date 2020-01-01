#!/usr/bin/env python3

import json
import csv
import sys

import django
from django.template import Template, Context
from django.conf import settings
from os import listdir
from os.path import isfile, join

settings.configure(TEMPLATES=[
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['.'], # if you want the templates from a file
        'APP_DIRS': False, # we have no apps
    },
])

django.setup()

input_path = sys.argv[1]
output_html=sys.argv[2]

template = """

    {% for results in matrix %}
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
                <tr class="result-{{ result.StatusCode }}" style="background-color: {{result.HTMLColor}};">
                <td><font color="black" class="status-code">{{ result.StatusCode }}</font></td>
                <td>{{ result.keyword }}</td>
                <td>{{ result.Url }}</td>
                <td>{{ result.RedirectLocation }}</td>
                <td>{{ result.Position }}</td>
                <td>{{ result.ContentLength }}</td>
                <td>{{ result.ContentWords }}</td>
                <td>{{ result.ContentLines }}</td>
                </tr>
            {{% end for %}}
        </tbody>
      </table>
    {{% end for %}}


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
    return results

def get_files_list(dir):
    files_list = [f for f in listdir(dir) if isfile(join(dir, f))]
    return files_list

def write_one_table(results):
    t = Template(template)
    c = Context(results)

    output = open(output_html,'w')
    output.write(t.render(c))
    output.close()

def main():

    files = get_files_list(input_path)
    matrix = [ read_csv(file) for file in files]

    for results in matrix:
        write_one_table(results)



if __name__ == '__main__':
    main()
