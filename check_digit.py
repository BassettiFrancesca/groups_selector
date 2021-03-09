def check_digit(digit, pairs_leaves):
    for pair in pairs_leaves:
        for p in pair:
            if digit in p:
                return True
    return False
