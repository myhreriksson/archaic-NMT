import sys
import re

pattern = r'\~\~\~\s*'

filename = f'{sys.argv[1]}_Conversation_{sys.argv[2]}.txt'
inp_path = f'data/preprocessed_tk_al/{filename}'
out_path = f'data/preprocessed_tk_al_cl/{filename}'

with (
    open(inp_path, 'r', encoding='utf-8') as i_f,
    open(out_path, 'w', encoding='utf-8') as o_f
    ):
    lines = i_f.readlines()
    for line in lines:
        line = re.sub(pattern, '', line)
        o_f.write(line)