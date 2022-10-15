flag = 0
even = 0
odd = 0
maxOdd=0
for i in range(0, 10):
    number = int(input())
    if number % 2 == 0 and flag == 0:
        max = number
        min = number
        flag = 1
    if number % 2 == 0 and flag == 1:
        even += 1
        if number > max:
            max = number
        if number < min:
            min = number
    if number % 2 != 0:
        odd += 1
        if number > maxOdd:
            maxOdd = number

print("min=%d" % min)
print("max=%d" % max)
print("oddCounter=%d" % odd)
print("maxOdd=%d" % maxOdd)
print("counter=%d" % even)

