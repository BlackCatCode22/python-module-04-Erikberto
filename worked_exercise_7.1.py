#Module 4
#Chapter 7 worked exercise 7.1
#eS 3/22/25
#CIT-95 spring25
fh = open('mbox-short.txt')

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())