import os
import sys

def _generate_definition(dir_, fpath):
    output = """<key>{0}</key>
    <dict>
        <key>Group</key>
        <string>{1}</string>
        <key>Path</key>
        <string>{2}</string>
    </dict>
    """.format(fpath, dir_, fpath)
    return output

def generate_definitions(dir_):
    definitions = []
    for root, dirs, files in os.walk(dir_):
        for file_ in files:
            fpath = os.path.join(root, file_)
            definition = _generate_definition(root, fpath)
            definitions.append(definition)
    return ''.join(definitions)


def _generate_node(fpath):
    output = "<string>{0}</string>".format(fpath)
    return output

def generate_nodes(dir_):
    nodes = []
    for root, dirs, files in os.walk(dir_):
        for file_ in files:
            fpath = os.path.join(root, file_)
            node = _generate_node(fpath)
            nodes.append(node)
    return '\n'.join(nodes)

