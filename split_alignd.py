import sys
import os

game_affix = sys.argv[1]

aligned_txt = f'data/parallel_tk_al/aligned_sents_{game_affix}.txt'
en_out = f'{game_affix}_Conversation_EN.txt'
de_out = f'{game_affix}_Conversation_DE.txt'
out_path = 'data/preprocessed_tk_al/'

with (
    open(aligned_txt, encoding="utf-8") as aligned,
    open(os.path.join(out_path, de_out), "w", encoding="utf-8") as de_o,
    open(os.path.join(out_path, en_out), "w", encoding="utf-8") as en_o
    ):
    for line in aligned:
        section = line.strip('\n').split('\t') # strip newlines and tabs and ake a section (list with en, de, confidence)
        if len(section) < 3: # in case line does not contain aligned sentences, continue
            continue
        de_sent = section[0]
        en_sent = section[1]
        de_o.write(de_sent + '\n')
        en_o.write(en_sent + '\n')