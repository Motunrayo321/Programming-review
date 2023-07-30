from validator_collection import validators, errors
import sys


def main():
    print(validate(input("Emaill Address: ")))


def validate(email):
    try:
        email = validators.email(email)
        return "Valid"

    except (errors.EmptyValueError, errors.InvalidEmailError):
        #print ("Please input a valid email address")
        return "Invalid"
    

while True:
    if __name__ == "__main__":
        main()