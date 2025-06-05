def _99bottles(numberOfBottles: int):
    print(f"""{numberOfBottles} bottles of beer on the wall, {numberOfBottles} bottles of beer.
        Take one down and pass it around, {numberOfBottles - 1} bottles of beer on the wall.""")
    if numberOfBottles > 1:
        _99bottles(numberOfBottles - 1)
    else:
        print("""No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
""")

_99bottles(4)