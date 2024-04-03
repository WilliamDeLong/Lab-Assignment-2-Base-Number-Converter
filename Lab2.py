baseValues=[0,1,2,3,4,5,6,7,8,9,"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
tests2run1 = [2024,2024,2024,1024,-155,250,4554,6756,2846]
tests2run2 = [2,8,16,12,4,18,8,25,21]
for numerical in range(len(tests2run1)):
    negative=False
    startingNum = tests2run1[numerical]
    print(f"Input a number to be used as the starting value\n> {startingNum}")
    base = tests2run2[numerical]
    print(f"Input a number to use as the base\n> {base}")
    decNum = startingNum
    if startingNum <0:
        decNum*=-1
        negative=True
    remainders = []
    numbers=[]
    loopNum=0
    print(f"{startingNum} calc'd in base {base}")

    while decNum>0:
        if loopNum%4==0:
            remainders.append(" ")
        remainders.append(str(decNum%base))
        decNum=int(decNum/base)
        numbers.append(decNum)
        loopNum+=1
    if negative:
        remainders.append("-")
    remainders2 = []
    for i in remainders:
        if i!=' ' and i!="-":
            remainders2.append(str(baseValues[int(i)]))
        else:
            remainders2.append(i)
    print(f'{startingNum} converted in its base {base} value is {"".join(remainders2[::-1])}\n\n(base) C:\\Users\wxmkt\Documents\Programming Language class>python "Lab2.py"\n')
