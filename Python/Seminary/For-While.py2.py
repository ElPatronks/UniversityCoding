index = 0
total = 0
sum=0
while True:
    low=int(input("low="))
    high=int(input("high="))

    if low < high:
        break
    else:
        print("Wrong limits!")
for i in range (0,10):
    a=int(input("a="))
    sum +=a
    total+=1
    if a >=low and a <= high:
        index +=1
print("index = %d" % index)
print("total = %d" % total)
print("sum = %d" % sum)
