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
cs
cs50
cs5p
csp50
csp5p
csp500
csp50w
'''

def end(s):
    n = s[:1:-1]
    count = len(n)
    flag = False

    if n[0].isalpha():
        flag = n[1:].alpha()
    if n[0].isdigit():

        if count == 1:
            flag = True

        if count == 2:
            flag = True

        if count == 3:
            if n[1].isdigit():
                flag = True

        if count == 4:
            if n[1].isdigit():
                if n[2].isdigit():
                    flag = True
                elif n[2].isalpha():
                    if n[3].isalpha():
                        flag = True

            elif n[1].isalpha():
                if n[2:].isalpha():
                    flag = True
                    

'''
            csppp0
            cspp00
            cs5p00

            csp500
            csp5p0
            csp500
            cs5500
            cs5500


    count = len(n)

    f = ''
    m = ''
    
    while count > 1:
        for i in n:
            if i.isalpha():
                f += i
            elif i.isdigit():
                m += i
            print ('1')
            
            count -= 1
    if f == n or m == n:
        print (True)
        return True
    else:
        print (False)
        return False
''' 
    


end("csp50")