file_path = "research/_filehandling/order.txt"
file = open(file_path, "w")

try:
    file.write("Masala chai - 2 cups")
finally:
    file.close()

with open(file_path, "a") as f:
    f.write("\nYour 2nd order is Ginger chai - 3 cups")