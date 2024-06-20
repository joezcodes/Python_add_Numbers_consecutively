#adds the 1st to the second
#Then adds that answer to the 3rd
#Then adds that answer to the fourth
#Then adds that answer to the fifth  

num1 = 12
num2 = 36
num3 = 57
num4 = 24
num5 = float(.12)

def addNumbers(*num):
    sum = 0
    for i in num:
         sum = sum + i
         print(sum)


addNumbers(num1,num2,num3,num4,num5)

#print(addNumbers())