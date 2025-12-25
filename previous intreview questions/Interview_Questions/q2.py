# WAP to return index of the target value

def search(ls: list[int], target: int) -> int:
    for idx, val in enumerate(ls):
        if val >= target:
            return idx
    return len(ls)

search([1,2, 3, 4, 5, 6], 7)
