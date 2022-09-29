#!/usr/bin/env python3

import argparse
import modules

def setup_parser():
    parser = argparse.ArgumentParser(description='TRecon - tool to analyze Domains and IPs.')
    subparsers = parser.add_subparsers()

    #bw
    bw = modules.builtwith()

    subparsersnew = bw.add_parser(subparsers)
    return subparsersnew


def main():
    parser = setup_parser()


    args = parser.parse_args()


if __name__ == "__main__":
    main()