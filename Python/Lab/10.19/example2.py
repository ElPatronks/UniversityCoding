sum =0
index =0
even = False
odd = False
while index <10:
    a=int(input("a="))
    sum += a
    index += 1
if sum % 2 == 0:
        even = True
elif sum % 2 !=0:
        odd = True

print(f"Even-{even}, Odd-{odd}")
print(f"sum = {sum}")  #print("sum=%d"%sum)
