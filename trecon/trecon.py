#!/usr/bin/env python3

import argparse
import sys
import modules

def setup_parser():
    parser = argparse.ArgumentParser(description='TRecon - tool to analyze Domains and IPs.')
    
    return parser


def main():
    parser = setup_parser()

    setup_modules(parser)
    if len(sys.argv) <= 1:
        sys.argv.append('--help')

    args = parser.parse_args()
    args.func()

def setup_modules(parser):
    subparser = parser.add_subparsers()
    bw = modules.builtwith()
    sh = modules.shodan()
    bw.add_parser(subparser)
    sh.add_parser(subparser)

if __name__ == "__main__":
    main()