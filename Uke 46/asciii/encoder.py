with open('hemmelig.txt', "r", encoding="utf-8") as f:
    for line in f:
        for word in line.split("|"):
            for c in word.split(','):
                if c.isdigit():
                    print(chr(int(c)), end='')
            print(' ', end='')
        print('')
