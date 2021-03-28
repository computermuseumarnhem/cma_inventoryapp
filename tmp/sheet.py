#!/usr/bin/env python3

import os

header = ["id", "wikilink", "Actie", "label", "manufacturer", "model", "name", "serial", "Location", "type", "Owner", "Status", "category",
          "Architecture", "System/interface bus", "OS", "", "", "Hostname", "IP", "DECnet", "Knowhow", "Origin", "Acquired", "MAC", "picture"]

categories = {
    'Calculator':                   'Calculator', 
    'Programmeerbare calculator':   'Calculator|Programmable', 
    'Boekhoudmachine':              'Calculator|Accounting', 

    'Desktop computer':             'Computer|Desktop', 
    'Workstation':                  'Computer|Workstation', 
    'Computer':                     'Computer', 
    'PC':                           'Computer|PC', 
    'Thin Client':                  'Computer|Thin Client', 
    'Server':                       'Computer|Server', 
    'Homecomputer':                 'Computer|Homecomputer', 
    'Portable computer':            'Computer|Portable', 
    'Laptop':                       'Computer|Laptop', 
    'Handheld':                     'Computer|Handheld', 
    'Portable':                     'Computer|Portable', 
    'PC “Pentium 4”':               'Computer|PC|Pentium 4', 
    'Minicomputer':                 'Computer|Mini', 

    'Storage':                      'Storage', 
    '3.5” floppy drive':            'Storage|Diskette|3.5"', 
    'Dual 8” floppy drive':         'Storage|Diskette|8"|dual', 
    '2x 3.5” floppy drive':         'Storage|Diskette|3.5"|dual', 
    'Disk':                         'Storage|Harddisk', 
    'CD-ROM/AUDIO Drive':           'Storage|CDROM|With audio', 

    'Typewriter':                   'Typewriter', 
    'Teleprinter':                  'Typewriter|Automatic', 

    'Terminal':                     'Terminal', 
    'Hardcopy terminal':            'Terminal|Hardcopy', 
    'Grafische terminal':           'Terminal|Graphical', 

    'Communications Server':        'Network|Server|Communication', 
    'Terminal Server':              'Network|Server|Terminal', 
    'Hub/switch RJ45':              'Network|Switch|Token-ring|RJ-45', 

    'Sound synthesizer':            'Sound synthesizer', 
    'Interface':                    'Interface', 
    'Modembank':                    'Modembank', 

    'Card Punch': 'Card punch', 
    'Scanner': 'Scanner', 
    'Keyboard': 'Keyboard', 
    'EPROM Programmer': 'EPROM Programmer', 
    'Toetsenbord': 'Keyboard', 
    'Systeemkast': 'System unit', 
    'Tekstverwerker': 'Word processor', 
    'Network device': 'Network', 
    'Monitor': 'Monitor', 
    'Input Device': 'Input Device', 
    'Voeding': 'Power supply', 
    'X.25 PAD': 'Networking|X.25 PAD', 
    'Plotter': 'Hardcopy|Plotter', 
    'Printer': 'Hardcopy|Printer', 
    'Telex': 'Telex', 
    'Parts': 'Parts'
}

def row():
    with open(os.path.join(os.path.dirname(__file__), 'sheet.txt')) as f:
        for line in f:
            items = dict(zip(header, (item.strip() for item in line.split('\t'))))

            for i in items:
                if not items[i]:
                    items[i] = None

            items['category'] = categories[items['type']] if items['type'] else None

            yield items

if __name__ == '__main__':
    for i in row():
        if i['picture']:
            print(i['picture'])