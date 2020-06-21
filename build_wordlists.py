all_words = {}

check_words = [set() for _ in range(16)]

with open("wrdr/wordlists/twl18_upper.txt", "w") as wl:
    with open("wrdr/wordlists/twl2018.txt", 'r') as f:
        for line in f:
            line = line.strip()
            line = line.upper()
            wl.write(line)
            wl.write("\n")
            for x in range(2,len(line)):
                stem = line[0:x]
                check_words[x].add(stem)



    for _ in range(2,15):
        with open("wrdr/wordlists/ck{}.txt".format(_), "w") as f:
            for word in sorted(check_words[_]):
                f.write(word)
                f.write("\n")





