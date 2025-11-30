class InvalidChaiError(Exception):...


def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"{flavor} chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")

        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: ₹ {total}")
    except Exception as e:
        print("Error", e)
    finally:
        print("Thank you for visiting chaiKiTapari!")

bill("masala", "two")
bill("mashrom", 3)
bill("masala", 3)
         
        