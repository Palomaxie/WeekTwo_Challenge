def the_square(num):
    square = num*num
    return square


dict_sq = {num: the_square(num) for num in range(1, 16)}

print(dict_sq)
