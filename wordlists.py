
def build_dicts():
    dicts = {}
    for i in range(2,15):
        dicts[i] = {}
        with open("../old/wrdr/word_lists/check{}.txt".format(i)) as f:
            for line in f:
                line = line.strip()
                dicts[i][line] = True
    valid_words = {} 
    with open("../old/wrdr/owl_word_list_only.txt") as f:
        for line in f:
            line = line.strip()
            valid_words[line] = True
            
    return (dicts, valid_words)