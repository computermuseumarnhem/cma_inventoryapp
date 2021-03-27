#!/usr/bin/env python3

import os

header = ["id", "wikilink", "Actie", "label", "manufacturer", "model", "name", "serial", "Location", "Type", "Owner", "Status", "Category",
          "Architecture", "System/interface bus", "OS", "", "", "Hostname", "IP", "DECnet", "Knowhow", "Origin", "Acquired", "MAC", "picture"]


def row():
    with open(os.path.join(os.path.dirname(__file__), 'sheet.txt')) as f:
        for line in f:
            items = dict(zip(header, (item.strip() for item in line.split('\t'))))

            for i in items:
                if not items[i]:
                    items[i] = None

            yield items

if __name__ == '__main__':
    for i in row():
        if i['picture']:
            print(i['picture'])