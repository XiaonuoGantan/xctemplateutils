#!/usr/bin/env python
"""Print to stdout a list of <key> and <dict> tags for a subfolder in xctemplate"""
import os
import sys

def generate_definitions(dir_, fpath):
    output = """<key>{0}</key>
    <dict>
        <key>Group</key>
        <string>{1}</string>
        <key>Path</key>
        <string>{2}</string>
    </dict>
    """.format(fpath, dir_, fpath)
    return output

if __name__ == '__main__':
    dir_ = sys.argv[1]
    definitions = []
    for root, dirs, files in os.walk(dir_):
        for file_ in files:
            fpath = os.path.join(root, file_)
            definition = generate_definitions(root, fpath)
            definitions.append(definition)
    sys.stdout.write(''.join(definitions))
