#!/usr/bin/env python

import argparse
from git import Repo

import configprocessor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Path to git working copy")
    parser.add_argument("-c", "--configfile", help="Configuration file to parse")
    parser.add_argument("-o", "--outputfile")
    args = parser.parse_args()

    branch = getCurrentBranch(args.path)
    configprocessor.run(args.configfile, args.outputfile, branch)

def getCurrentBranch(path):
    repo = Repo(path)
    branch = repo.active_branch
    return branch

if __name__ == "__main__":
    main()
