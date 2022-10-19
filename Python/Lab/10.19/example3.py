sum = 0
br =0
while True:
    a=int(input("a="))
    if a > 0:
        br +=1
    if a == -99:
        break
    if a < 0:
        continue
    sum+=a
print(f"sum={sum}")   #print(f"sum=%d" % sum)
print(f"positive numbers {br}")
