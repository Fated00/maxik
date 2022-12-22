def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y


flag = True
file = open("unit.txt")
while flag:
    line = file.readline()
    if not line:
        flag = False

    if '+' in line:
        ind = line.find('+')
        print(addition(int(line[:ind]), int(line[ind + 1:])))

    if '-' in line:
        ind = line.find('-')
        print(subtraction(int(line[:ind]), int(line[ind + 1:])))

    if '*' in line:
        ind = line.find('*')
        print(multiplication(int(line[:ind]), int(line[ind + 1:])))

    if '/' in line:
        ind = line.find('/')
        print(division(int(line[:ind]), int(line[ind + 1:])))
