import string
import random

if __name__ == "__main__":
    str_1 = string.ascii_lowercase
    str_2 = string.ascii_uppercase
    str_3 = string.digits
    str_4 = string.punctuation

    data = int(input("Enter password length\n"))
    str = []

    str.extend(list(str_1))
    str.extend(list(str_2))
    str.extend(list(str_3))
    str.extend(list(str_4))
    print("Your password is: ")
    print("".join(random.sample(str, data)))
