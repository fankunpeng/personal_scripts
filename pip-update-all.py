#! /usr/bin/python3.5 
import os
import re
import argparse
parser = argparse.ArgumentParser(description='upgrade all packages outdated')
parser.add_argument('edition', help='the edition of your pip, such as a, 3')
args = parser.parse_args()

os.system('pip' + args.edition + ' list --outdated > ./tmp')
pack_match = re.compile(r'^([a-zA-Z0-9-]*) .* - .*')
with open('./tmp', 'rt') as f:
    for line in f:
        u = pack_match.match(line)
        if u:
            print(u.group(1))
#            print(type(u.group(1)))
            os.system('pip' + args.edition + ' install -U ' + u.group(1))

os.system('rm ./tmp')
