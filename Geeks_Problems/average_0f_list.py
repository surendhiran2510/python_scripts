#Average numbers in arays

list= [1,2,3,4,5,6,7,8,9,10,11]
sum = 0
n =len(list)

print(range(n))
for i in range(n):
    sum += list[i]
    i = i + 1
print (f"average of list : {sum/n}")
