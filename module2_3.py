my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
while x + 1 <= len(my_list):
    if my_list[x] == 0:
        pass
    elif my_list[x] > 0:
        print(my_list[x])
    else:
        break
    x += 1
