#%% Type hinting

def addisjon(tall1, tall2, tall3):
    if isinstance(tall1, int) and isinstance(tall2, int) and isinstance(tall3, int):
        return tall1 + tall2 + tall3
    return None


print(addisjon(2, 3, 5))

#%% *args


def addisjon2(*args):
    print(sum(args))


addisjon2(2, 4, 6, 8)
