def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {int(cost)}")
    except KeyError:
        print("Sorry that chai is not in menu")
    except TypeError:
        print("Quantity must be in number")
    except ValueError:
        print("It's not an integer")
    except Exception as e:
        print(e)
        


process_order("ginger", 2)
process_order("masala", "two")
