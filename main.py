#!/usr/bin/python3
# main.py
import argparse
import re

import pydeepl
import pysrt

# Argument Parsing
description = """
Translate an SRT file from and to the following languages:
English, French, German, Spanish, Italian, Dutch, Polish
"""
epilogue = """
Input and Output modes: 
auto\t Auto Detect (only for input)\n
DE\t German\n
EN\t English\n
FR\t French\n
ES\t Spanish\n
IT\t Italian\n
NL\t Dutch\n
PL\t Polish\n
"""
parser = argparse.ArgumentParser(description=description, epilog=epilogue)
parser.add_argument('infile', nargs='?', help = "input file: in.srt")
parser.add_argument('outfile', nargs='?', help = "output file: out.srt")
parser.add_argument('-d', '--in_lang', nargs='?', help = "Input Language")
parser.add_argument('translateto', nargs='?', help = "Output Language")
args = vars(parser.parse_args())

# Subtitle reading
lines = pysrt.open(args['infile'])
# for i in lines:
#     i.text = re.sub("<[^>]*>", '', i.text)
#     print(i.text)
index = 0
sentence = ""
begin_index = 0
while index < len(lines):

    words = re.findall(r"[\w']+|[.!?]", re.sub("<[^>]*>", '', lines[index].text))
    lines[index].text = ""
    # find last occurrence of a punctuation mark in the words
    index_last_punctuation = -1
    for i in reversed(list(range(len(words)))):
        if re.match("[.!?]", words[i]):
            index_last_punctuation = i
            break
    # if there is no punctuation in this sentence, then add the complete subtitle line to string sentence
    if (index_last_punctuation == -1):
        sentence += " ".join(words)
    else:
        sentence += (" ".join(words[0:index_last_punctuation + 1]) + " ")
        if (args["in_lang"] == None):
            from_lang = "auto"
        else:
            from_lang = args["in_lang"]
        translated_sentence = pydeepl.translate(sentence, args['translateto'], from_lang=from_lang)
        # Insert translated sentences into the subtitle file.
        list_trans_sents = translated_sentence.split()  # translated sentences in list form
        list_trans_sents.insert(int(len(list_trans_sents)/2), "\n")
        width = int(1 + len(list_trans_sents) / (index - begin_index + 1))  # number of words per line
        for i in list(range(index - begin_index + 1)):
            phrase = " ".join(list_trans_sents[i * width:width * (i + 1)])
            print(phrase)
            lines[index].text += phrase + "\n"
        # If the sentence ends with a punctuation mark, then the sentence string should be empty
        # Else the sentence string should contain the text up to the end of the string

        if index_last_punctuation + 1 == len(words):
            sentence = ""
            begin_index = index + 1
        else:
            sentence = (" ".join(words[index_last_punctuation + 1:len(words)]) + " ")
            begin_index = index

    index += 1
lines.save(args['outfile'])
