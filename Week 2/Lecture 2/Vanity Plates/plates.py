def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag = False

def length(s):
    if 2 <= len(s) <= 6:
        return True

def alpha(s):
    count = 0
    for i in s:
        if i.isalpha:
            pass
        if count >= 2:
            return True

'''
cs Y
cs50 Y
cs5p N
csp50 Y
csp5p N
csp500 Y
csp50w N
'''

def end(s):
    n = s[:1:-1]
    m = s[2:]
    count = len(n)
    flag = False

    if n[0].isalpha():
        flag = n[1:].isalpha()
    if n[0].isdigit():

        if count == 1:
            flag = True

        if count == 2:
            flag = True

        if count == 3:
            if n[1].isdigit():
                if n[2].isdigit and n[2] != 0:
                    flag == True


        if count == 4:
            if n[1].isdigit():
                if n[2].isdigit():
                    if n[3] != 0:
                        flag = True

                else:
                    if n[2] != 0 and n[3].isalpha():
                        flag = True
                    

            else:
                if n[1] != 0 and n[2:].isalpha():
                    flag = True
    
    print (flag)

'''
            cspppp Y
            csppp0 Y
            cspp0p N
            csp0pp N
            cs0ppp N
            cspp00 Y
            csp00p N
            cs00pp N
            csp0p0 N
            cs0pp0 N
            cs0p0p N
            csp000 Y
            cs000p N
            cs00p0 N
            cs0p00 N
            cs0000 Y
''' 
    

while True:
    end(input("Plate Number: "))