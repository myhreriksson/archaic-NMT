import sys
import re
import os
import chardet # for detecting file encoding

#--------------------PART 1: File Decoding--------------------#
# DETECT ENCODING
def det_enc(path):
    with open(path, 'rb') as f:
        raw = f.read()
        result = chardet.detect(raw)
        return result['encoding']

game_prefix = sys.argv[1]
lang_suffix = sys.argv[2]

# GLOBAL VARIABLES
inp_path = f'data/untokenized/{game_prefix}/{lang_suffix}/'
out_path = 'data/tokenized/'
out_file = f'{game_prefix}_Conversation_{lang_suffix}.txt'
out_fullpath = os.path.join(out_path, out_file)
corpus = list()

# CONVERT ENCODING
for file in sorted(os.listdir(inp_path)):
    inp_fullpath = os.path.join(inp_path, file)
    encoding = det_enc(inp_fullpath)

    with (open(inp_fullpath, 'r', encoding=encoding) as f_i,):        
        txt = f_i.read()
        if re.search('   ', txt[0:100]): # if spacing from utf-16-le or "ansi" encoding remains, then:
            txt = re.sub('   ', '_', txt) # substitute word token separators
            txt = re.sub(' ', '', txt) # substitute char separators
            txt = re.sub('_', ' ', txt) # substitute word token separators again

#--------------------PART 2: Sentence Tokenizing--------------------# 
# OVERWRITE: LINE BY LINE
        pattern_1 = r'(?<!(?:\.{2}))(?<=[.!?])\s+' # splits at singular exclamations and dots; keeps clauses and tripple dots
        pattern_2 = r'\s+([.,!?])' # removes spaces before tripple dots
        pattern_3 = r'\.+(\.{3})' # replaces long dot strings with tripple dots (OSÄKER OM FUNKAR; DUBBELKOLLA NÄR TID FINNS)
        pattern_4 = r'\s*\n\s*' # removes spaces before and after newlines
        pattern_5 = r'\&' # correctly replaces ambersands with tripple dots; double-checked in-game
        pattern_6 = r'\.\.\.\s*(\w)' # adds space after tripple dot if there is none
        pattern_7 = r'(\(no line\)|\(N\/A\)|\(dummyText\))' # removes useless tags
        pattern_8 = r'<.*>' # removes non-conversational descriptions
        
        lines = re.split(pattern_1, txt)

        for i, line in enumerate(lines):
            line = re.sub('\n', ' ', line)
            line = re.sub(pattern_2, r'\1', line)
            line = re.sub(pattern_3, r'\1', line)
            line = re.sub(pattern_4, '\n', line)
            line = re.sub(pattern_5, '...', line) # kan behöva flytta den här
            line = re.sub(pattern_6, r'... \1', line)
            line = re.sub(pattern_7, '', line)
            line = re.sub(pattern_8, '', line)
            if len(line.strip()) > 0:
                corpus.append(line.strip())
            else:
                continue

#--------------------PART 3: Write Corpus to File--------------------#
with open(out_fullpath, 'w', encoding='utf-8') as o_f:
    for sent in corpus:
        o_f.write(sent + '\n')