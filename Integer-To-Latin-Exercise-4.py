from collections import OrderedDict

def latinikoi_Xaraktires(num):
    latinikos = OrderedDict()
    latinikos[1000] = "M"
    latinikos[900] = "CM"
    latinikos[500] = "D"
    latinikos[400] = "CD"
    latinikos[100] = "C"
    latinikos[90] = "XC"
    latinikos[50] = "L"
    latinikos[40] = "XL"
    latinikos[10] = "X"
    latinikos[9] = "IX"
    latinikos[5] = "V"
    latinikos[4] = "IV"
    latinikos[1] = "I"

    def latinikos_arithmos(num):
        for r in latinikos.keys():
            x, y = divmod(num, r)
            yield latinikos[r] * x
            num -= (r * x)
            if num > 0:
                latinikos_arithmos(num)
            else:
                break

    return "".join([a for a in latinikos_arithmos(num)])

num=input("Enter a number: ")
while (num<1 or num>1000000):
    print "Number range is 1-1000000"
    num=input("Re-enter a number: ")
print (latinikoi_Xaraktires(num))
