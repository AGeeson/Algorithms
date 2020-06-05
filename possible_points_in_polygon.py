length_p = float(100)
width_p = float(20)
d = distance_between_points = float(5)

area_p = length_p * width_p

2*d+d
i= 0
j=0
k=0
l=0
while True:
    if i+(2*d) > length_p:
        break 
    if j == 0:
        i+= 2*d+d
        j+=1
    else:
        i+=2*d
        j+=1
    print(i,",",j)
excess = length_p - i
print(excess)

for p in range(10):
    print("\b-")
while True:
    if k+(2*d) > width_p:
        break
    if l == 0:
        k+= 2*d+d
        l+=1
    else:
        k+=2*d
        l+=1
    print(k,",",l)
excess2 = width_p - k
print(excess2)

