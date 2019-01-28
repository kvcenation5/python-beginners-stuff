 #simple calculator
calc = str(input('''Please enter the arithmetic operation: 
                   1. addition
                   2. subtraction
                   3. Miltiplication
                   4. Division \n '''  ))
arithmetic = True

digits = int(input( ''' Please enter whether you need to add two or three numbers
                            a) 2
                            b) 3 \n\n''' ))

while calc == '1' and arithmetic:
    if digits == 2:
        a = int(input("Please enter the first number \n "))
        b = int(input("Please enter the second number \n "))
        c = int(a + b) 
        c = str(c)
        print(" The value is " + c)
        arithmetic = False

    else:
        a = int(input("Please enter the first number \n"))
        b = int(input("Please enter the second number \n"))
        c = int(input("Please enter the third number \n"))
        d = int(a + b + c)
        d = str(d)
        print(" The  arithmetic Value is " + d)
        arithmetic = False

while calc == '2' and arithmetic:
    if digits == 2:
        a = int(input("Please enter the first number \n "))
        b = int(input("Please enter the second number \n "))
        c = int(a - b) 
        c = str(c)
        print(" The  arithmetic value is " + c)
        arithmetic = False

    else:
        a = int(input("Please enter the first number \n"))
        b = int(input("Please enter the second number \n"))
        c = int(input("Please enter the third number \n"))
        d = int(a - b - c)
        d = str(d)
        print(" The  arithmetic Value is " + d)
        arithmetic = False

while calc == '3' and arithmetic:
    if digits == 2:
        a = int(input("Please enter the first number \n "))
        b = int(input("Please enter the second number \n "))
        c = int(a * b) 
        c = str(c)
        print(" The  arithmetic value is " + c)
        arithmetic = False

    else:
        a = int(input("Please enter the first number \n"))
        b = int(input("Please enter the second number \n"))
        c = int(input("Please enter the third number \n"))
        d = int(a * b * c)
        d = str(d)
        print(" The  arithmetic Value is " + d)
        arithmetic = False

while calc == '4' and arithmetic:
    if digits == 2:
        a = int(input("Please enter the first number \n "))
        b = int(input("Please enter the second number \n "))
        c = int(a / b) 
        c = str(c)
        print(" The  arithmetic value is " + c)
        arithmetic = False

    else:
        a = int(input("Please enter the first number \n"))
        b = int(input("Please enter the second number \n"))
        c = int(input("Please enter the third number \n"))
        d = int(a / b / c)
        d = str(d)
        print(" The  arithmetic Value is " + d)
        arithmetic = False
