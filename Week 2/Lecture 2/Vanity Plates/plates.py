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
            
    


end("csp50")