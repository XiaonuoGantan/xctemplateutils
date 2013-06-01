#!/usr/bin/env python
import argparse
import sys

from xctemplateutils.generate_utils import generate_definitions, generate_nodes


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate XML elements that can be inserted into a .xctemplate file.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-d', type=str,
        help='Generate a list of <key> and <dict> elements that can be inserted into the <Definitions> element.')
    group.add_argument(
        '-n', type=str,
        help='Generate a list of <string> elements that can be inserted into the <Nodes> element.')
    args = parser.parse_args()
    if args.d:
        output = generate_definitions(args.d)
    elif args.n:
        output = generate_nodes(args.n)
    sys.stdout.write(output)

