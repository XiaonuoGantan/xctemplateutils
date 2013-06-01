#!/usr/bin/env python
"""Print to stdout a list of <string> tags for a subfolder in xctemplate"""
import os
import sys

def generate_definitions(fpath):
    output = "<string>{0}</string>".format(fpath)
    return output

if __name__ == '__main__':
    dir_ = sys.argv[1]
    definitions = []
    for root, dirs, files in os.walk(dir_):
        for file_ in files:
            fpath = os.path.join(root, file_)
            definition = generate_definitions(fpath)
            definitions.append(definition)
    sys.stdout.write('\n'.join(definitions))
