#!/usr/bin/env python3

import sheet

for item in sheet.row():

    if item['picture']:
        print(item)
        print()