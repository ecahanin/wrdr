import os
from django.conf import settings


def build_dicts():
    dicts = {}
    for i in range(2,15):
        dicts[i] = {}
        with open(os.path.join(settings.BASE_DIR, 'wordlists/check{}.txt'.format(i)), 'r') as f:
            for line in f:
                line = line.strip()
                dicts[i][line] = True
    valid_words = {} 
    with open(os.path.join(settings.BASE_DIR, 'wordlists/owl_word_list_only.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            valid_words[line] = True
            
    return (dicts, valid_words)