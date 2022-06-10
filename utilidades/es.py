def float_o_int(n=str()):
    numypunto = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    if len(n.split('.')) > 2:
        return False
    for car in n:
        if car not in numypunto:
            return False
    return True
