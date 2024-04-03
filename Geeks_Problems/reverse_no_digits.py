digit = "123"
length = len(digit)
new=[]
new_digit = digit[::-1]
for i in range(length):
    digit[i] = new[(-(i))]
print(new)
print(new_digit)