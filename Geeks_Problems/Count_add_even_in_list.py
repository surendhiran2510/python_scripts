list = [10,2,3,4,5,6,7,8,9]

add_count = 0

eve_count = 0

n = len(list)

for i in range(n):
    if list[i] % 2 == 0:
        eve_count += 1
        i += 1
    else:
        add_count += 1
        i += 1
print (f"eve_count: {eve_count} and add_count: {add_count}")