#Module 4
#Chapter 8 Strings, Files, List and Guardian Pattern
#eS 3/22/25
#CIT-95 spring25
han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])