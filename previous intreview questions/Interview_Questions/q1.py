# WAP to check the words present in the string (if they are similar)

def check(ls: list[str]):
    min_iter = min([len(i) for i in ls]) 
    new_s = ""
    for i in range(min_iter):
        new_set = set()
        for item in ls:
            new_set.add(item[i])
        if len(new_set)==1:
            new_s += ls[0][i]
        else:
            break
    
    return new_s


check(["flower", "flowing", "flows", "flowering"])
