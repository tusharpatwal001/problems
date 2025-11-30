class OutOfIngredientsError(Exception):
    pass


def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichai"]:
        raise OutOfIngredientsError("Unsupported chai flovor...")
    print(f"Brewing {flavor} chai...")


def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print(f"Chai is ready...")


brew_chai("masala")
make_chai(1, 0)
