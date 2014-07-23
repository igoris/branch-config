#!/usr/bin/env python

import sys
import re
import argparse
import ConfigParser

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--configfile", help="Configuration file to parse")
    parser.add_argument("-o", "--outputfile")
    parser.add_argument("-s", "--select", help="Select configuration")
    args = parser.parse_args()

    run(args.configfile, args.outputfile, args.select)

def run(configfile, outputfile, select):
    config = parse(configfile, select)
    writeConfig(config, outputfile, select)

def parse(configPath, selectedConfig):
    config = ConfigParser.RawConfigParser()
    config.optionxform=str

    config.read(configPath)

    sections = config.sections()

    expanded_section = getClosestSection(selectedConfig, sections)
    api = config.items(expanded_section)

    return api

def getClosestSection(selectedConfig, sections):
    for section in sections:
        section_r = "^"+section+"$"

        r = re.search(section_r, selectedConfig)
        if r:
            return section
    return None

def writeConfig(config, outputPath, configName):
    outputFile = open(outputPath, 'w')

    outputFile.write("/* This file was generated automatically. DO NOT MODIFY IT */\n")
    outputFile.write("#ifndef __CONFIG_%s__\n" % configName)
    outputFile.write("#define __CONFIG_%s__\n" % configName)

    for name,value in config:
        outputFile.write("#define %s %s\n" % (name, value))

    outputFile.write("#endif\n")

    outputFile.close()

if __name__ == "__main__":
    main()
