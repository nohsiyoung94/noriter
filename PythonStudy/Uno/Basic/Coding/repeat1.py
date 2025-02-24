input_num = input('please input number you want : ')
print("")
for idx in range(0, len(input_num)):
    ch = input_num[idx]
    numDollar = int(ch)
    strDollar = ""
    for idxDollar in range(0, numDollar):
        strDollar += "$"
    print(numDollar," : ",strDollar)    
    print("")
