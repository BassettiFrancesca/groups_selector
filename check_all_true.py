def check_all_true(bool_d):
    for i in range(len(bool_d)):
        if not bool_d[i]:
            return False
    return True
