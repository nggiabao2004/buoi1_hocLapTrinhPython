password=int(input("Nhap password: "))
password=[]

import re
def check_password(password):
    if len(password) < 6:
        return False
    if len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True