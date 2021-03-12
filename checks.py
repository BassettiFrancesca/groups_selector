def check_all_true(bool_d):
    for i in bool_d:
        if not bool_d[i]:
            return False
    return True


def check_digit(digit, pairs_leaves):
    for pair in pairs_leaves:
        for p in pair:
            if digit in p:
                return True
    return False


def check_duplicate(pair, pairs_list):
    for p in pairs_list:
        if p == pair:
            return True
    return False


def check_how_many(bool_d):
    false = 0
    for i in range(len(bool_d)):
        if not bool_d[i]:
            false += 1
    return false


def find_key(d, v):
    for i in d:
        if d[i] == v:
            return i


def str_to_pair(s, pairs):
    for p in pairs:
        if str(p) == s:
            return p
