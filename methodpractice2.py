def hello(parrot):
    print("This parrot" + parrot)




parrots = [" is bereft of life", " has joined the choir invisible", " is an ex-parrot"]

for parrot in parrots:
    hello(parrot)


def deadparrot(name):
    print("This is the " + name)
    hello(parrot)

deadparrot("Dead Parrot Sketch")
