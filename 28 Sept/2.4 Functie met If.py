def new_password(oldpassword: str,newpassword: str):
    if (oldpassword == newpassword) or (len(newpassword)<6):
        return False
    else:
        for x in range(0,9):
            if str(x) in newpassword:
                return True
        return False

print(new_password('apples','pears'))
print(new_password('apples','apples'))
print(new_password('apples','bananas'))
print(new_password('apples','bananas2'))