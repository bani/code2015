import csv
import json
from collections import OrderedDict

def rank(filename):
    with open('%s.csv' % filename,'rU') as csvfile:
        d = csv.DictReader(csvfile, dialect='excel', delimiter=',')
        t = percentage_and_transpose(d)
        with open('%s.json' % filename,'w') as js:
            json.dump(t, js)

def percentage_and_transpose(d):
    headers = list(d.fieldnames)
    headers.remove('total')
    headers.remove('Ward')

    targets = {}
    for key in headers:
        targets[key] = {}

    for row in d:
        total = float(row['total'])
        for k in headers:
            targets[k][row['Ward']] = int(row[k])/total

    for key in headers:
        targets[key] = OrderedDict(sorted(targets[key].items(), key=lambda t: -t[1])).keys()

    return targets

if __name__ == "__main__":
    rank('census-age-group')
    rank('census-mother-tongue')
