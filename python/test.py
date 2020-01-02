import json
import csv
import sys
import ast

from os import listdir
from os.path import isfile, join
from jinja2 import Template




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
                <tr class="result-{{ result["status_code"] }}" style="background-color: {{result["HTMLColor"]}};">
                <td><font color="black" class="status-code">{{ result["status_code"] }}</font></td>
                <td>{{ result.FUZZ }}</td>
                <td>{{ result.url }}</td>
                <td>{{ result["redirectlocation"] }}</td>
                <td>{{ result["position"] }}</td>
                <td>{{ result["content_length"] }}</td>
                <td>{{result['content_words']}}</td>
                </tr>
            {% endfor %}
        </tbody>
      </table>

"""




if __name__ == '__main__':
    a = csv.DictReader(open('E:\Scripts\python\developer.sumup.com', 'r'))
    results = [dict(d) for d in a]

    output_html = 'test.html'
    output = open(output_html,'w')

    template = Template(template_fraction)

    output.write(template.render(results=results))

    output.close()