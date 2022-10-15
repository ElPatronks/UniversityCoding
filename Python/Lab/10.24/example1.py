str=input()
str1= str*2
print(str1)
add=input()
str2=str+add
x = str2.replace(str2, "golqm magiosnik")
print(f"{x}")
for i in range(0,len(str)):
    print(str[i])
fstr = input()
n=str.find(fstr)
if n!=-1:
    print(f"{fstr} is on position {n+1} in string {str}") #n+1 зависи откъде броим от 0 или 1
else:
    print(f"{fstr} is not in the string {str}")
