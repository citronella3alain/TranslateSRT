#!/usr/bin/python3
# main.py
import argparse
import sys
import pysrt
import re
import pydeepl

# Argument Parsing
parser = argparse.ArgumentParser(description='Translate an SRT file')
parser.add_argument('infile', nargs='?')
parser.add_argument('-o', '--outfile', nargs='?')
parser.add_argument('-d', '--in_lang', nargs='?')
parser.add_argument('translateto', nargs='?')
args = vars(parser.parse_args())

# Subtitle reading
lines = pysrt.open(args['infile'])
# for i in lines:
#     i.text = re.sub("<[^>]*>", '', i.text)
#     print(i.text)

index = 0
sentence = ""
begin_index = 0
punctuation = [".","!","?"]
while index < len(lines):

    words = re.findall(r"[\w']+|[.!?]", re.sub("<[^>]*>", '', lines[index].text))
    #print(words)
    # find last occurrence of a punctuation mark in the words
    index_last_punctuation = -1
    for i in reversed(list(range(len(words)))):
        if (re.match("[.!?]", words[i])):
            index_last_punctuation = i
            break
    #print(index_last_punctuation)
    # if there is no punctuation in this sentence, then add the complete subtitle line to string sentence
    if (index_last_punctuation == -1):
        sentence += " ".join(words)
    else:
        sentence += (" ".join(words[0:index_last_punctuation+1]) + " ")
        print(sentence)
        translated_sentence = pydeepl.translate(sentence, args['translateto'])
        print(translated_sentence)
        # If the sentence ends with a punctuation mark, then the sentence string should be empty
        # Else the sentence string should contain the text up to the end of the string
        if (index_last_punctuation + 1 == len(words)):
            sentence = ""
        else:
            sentence = (" ".join(words[index_last_punctuation + 1:len(words)]) + " ")

    index += 1
