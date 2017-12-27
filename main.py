#!/usr/bin/python3
# main.py
import argparse
import sys
import pysrt
import re
parser = argparse.ArgumentParser(description='Translate an SRT file')
parser.add_argument('-i', '--infile', nargs='?')
parser.add_argument('-o', '--outfile', nargs='?')
parser.add_argument('-d', '--in_lang', nargs='?')
parser.add_argument('translate_to', nargs='?')
args = vars(parser.parse_args())
srt = ""
if args['infile'] is None:
    srt = sys.stdin
else:
    srt = pysrt.open(args['infile'])
    #inf = open(args['infile'], 'r')
    #srt = inf.read()
    #inf.close()
#print(srt)
#subs = pysrt.open(srt)
for i in srt:
    i.text = re.sub("<[^>]*>", '', i.text)
    print(i.text)