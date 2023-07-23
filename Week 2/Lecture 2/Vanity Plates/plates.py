"""
 Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""

"""
Test Cases
length
    c       N
    w       N
    sd      Y
    sfg     Y
    myname  Y
    iamher  Y
    hisname N
    whythem N

first_two_alpha
    a3 N
    45 N
    3t N
    qw Y
    am Y

end
    cs Y
    cs50 Y
    cs5p N
    csp50 Y
    csp5p N
    csp500 Y
    csp50w N

    cspppp Y Y
    csppp0 Y N
    csppp1 Y Y
    cspp0p N N
    cspp1p N N
    csp0pp N N
    csp1pp N N
    cs0ppp N N
    cs1ppp N N
    cspp00 Y N
    cspp10 Y Y
    csp00p N N
    csp10p N N
    cs00pp N N
    cs10pp N N
    csp0p0 N N
    csp1p0 N N
    cs0pp0 N N
    cs1pp0 N N
    cs0p0p N N
    cs1p0p N N
    csp000 Y N
    csp100 Y Y
    cs000p N N
    cs100p N N
    cs00p0 N N
    cs10p0 N N
    cs0p00 N N
    cs1p00 N N
    cs0000 Y N
    cs1000 Y Y


all_alpha
    swee.t N
    cs50. N
    glam! N
    gas? N
    whyme? N
    no_gas N
    l00k N
    [mine] N
    sweet Y
    cs50 Y
    glam Y
    gas Y
    lk00 Y


"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    flag = False

    print (f"1. {length(s)}")
    print (f"2. {first_two_alpha(s)}")
    print (f"3. {end(s)}")
    print (f"4. {all_alpha(s)}")

    if length(s) and first_two_alpha(s) and end(s) and all_alpha(s):
        return True

def length(s):
    flag = False

    if 2 <= len(s) <= 6:
        flag = True

    return flag

def first_two_alpha(s):
    flag = False

    if s[:2].isalpha():
        flag = True

    return flag

def end(s):
    flag = False

    n = s[:1:-1]
    m = s[2:]
    count = len(n)

    if len(s) < 3:
        flag = True
        return flag

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
    
    #print (flag)
    return flag


def all_alpha(s):
    flag = False

    if s.isalnum():
        flag = True
    
    return flag 
    

while True:
    main()