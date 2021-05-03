Text = "kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd."
Alpha = ["a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
res = []
for i in Alpha:
    print(str(i) + ":" + str(Text.count(i)))

A = 1

for i in Text:
    if i in Alpha:
        nb = Alpha.index(i)
        if nb != len(Alpha) - 1:
            print(Alpha[nb + A], end="")
        else:
            print(Alpha[A-1], end="")
    else:
        print(i, end="")

print(Alpha[:8])