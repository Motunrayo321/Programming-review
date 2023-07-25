"""
 Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
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
    print (f"2. {all_alnum(s)}")
    print (f"3. {first_two_alpha(s)}")
    print (f"4. {first_zero(s)}")
    print (f"5. {last_alpha(s)}")
    
    if length(s) and all_alnum(s) and first_two_alpha(s) and first_zero(s) and last_alpha(s):
        return True


def all_alnum(s):
    flag = False

    if s.isalnum():
        flag = True
    
    return flag 

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


def first_zero(s):
    flag = False

    m = s[2:]

    if m == '':
        flag = True

    for i in m:
        if i.isdigit():
            if i != '0':
                flag = True
                break
            else:
                break
        else:
            flag = True
            break

    #print (flag)
    return flag

def last_alpha(s):

    flag = False
        
    if len(s) >= 2:
        for i in range(len(s)-1):
            if s[i].isdigit():
                if s[i+1].isalpha():
                    flag = False
                else:
                    flag = True
            else:
                flag = True

    return flag

while True:
    main()