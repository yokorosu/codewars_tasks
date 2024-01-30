def narcissistic(value):
    tvalue = value
    resvalue = value
    k = 0
    sum_digits = 0
    while tvalue != 0:
        k += 1
        tvalue //= 10
    while value != 0:
        sum_digits += ((value % 10) ** k)
        value //= 10
    if sum_digits == resvalue:
        return True
    return False

print(narcissistic(153))
