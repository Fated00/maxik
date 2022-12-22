def sum(x1, x2):
    return x1 + x2
def mul(x1, x2):
    return x1 * x2
def sub(x1, x2):
    return x1 - x2
def div(x1, x2):
    if x2 != 0:
      return x1/x2
def modd(x1,x2):
    if x2 != 0:
        return x1%x2


summa = 0

File = open("unit.txt") 
p = File.readlines()
for i in range(len(p)):
    str = p[i]
    if "+" in str:
        for j in range(len(str)-1):
            if str[j] == "+":
                summa = j
        print(sum(int(str[:summa]),int(str[summa+1:])))
    if "*" in str:
        for j in range(len(str) - 1):
            if str[j] == "*":
                summa = j
        print(mul(int(str[:summa]), int(str[summa+1:])))
    if "-" in str:
        for j in range(len(str) - 1):
            if str[j] == "-":
                summa = j
        print(sub(int(str[:summa]), int(str[summa+1:])))
    if "/" in str:
        for j in range(len(str) - 1):
            if str[j] == "/":
                summa = j
        print(div(int(str[:summa]), int(str[summa+1:])))