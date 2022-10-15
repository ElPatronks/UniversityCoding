array=()
for i in range(0, 5):
    x=int(input("x="))
    array = array + (x,)
print(array)
array1=array*2
print(f"double: {array1}")
key=int(input("Searching element:"))
if key in array:
    print(f"{key} is in the array")
else:
    print(f"{key} is not in the array")
for i in range (0,int(input()):
    print(array[i])
min_el=min(array)
print(f"min={min_el}")
