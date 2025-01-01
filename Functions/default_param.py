def calc_sum(a = 7, b = 32):
    calc_sum = a+b
    print(calc_sum)
    return calc_sum

calc_sum()

calc_sum(2,4)


def calc_prod(a, b=2):  # default argument comes after non-default
    calc_prod = a*b
    print(calc_prod)
    return calc_prod

calc_prod(7)