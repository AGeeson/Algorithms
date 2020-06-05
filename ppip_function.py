def pip(length_p, width_p, d):
    i=j=k=l=0
    while True:
        if i+(2*d) > length_p:
            break 
        if j == 0:
            i+= 2*d+d
            j+=1
        else:
            i+=2*d
            j+=1
    excess_l = length_p - i

    while True:
        if k+(2*d) > width_p:
            break
        if l == 0:
            k+= 2*d+d
            l+=1
        else:
            k+=2*d
            l+=1
    excess_w = width_p - k
    total_excess = excess_w+j + excess_l*l
    area = length_p*width_p
    percent_excess = (total_excess/area)*100
    print("Possible points in polygon is: " + str(l*j))
    print("with excess space of: "  + str(total_excess) + "cmxcm or " + str(percent_excess) )

pip(,10,6)
pip(100,35,5)
pip(1000,30,7)