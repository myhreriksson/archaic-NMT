#!/bin/bash

./hunalign/src/hunalign/hunalign -text \
  hunalign/src/hunalign/null.dic \
  data/tokenized/${1}_Conversation_EN.txt \
  data/tokenized/${1}_Conversation_DE.txt > data/parallel_tk_al/aligned_sents_${1}.txt
