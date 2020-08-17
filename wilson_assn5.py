"""
1) Prompt user for password
2) Tell user if password meets parameters

Parameters:
* Greater than 4 characters, less than 9 characters
* Cannot use "UMGC" in password
* Must contain '#' somewhere beyond the first or last position
"""

# Take user input for password
print('Please input password: ')
passwd = input()


def passwd_check(passwd):
    ret_val = True

    if len(passwd) < 4:
        print('Length should be at least 4 characters.')
        ret_val = False

    if len(passwd) > 9:
        print('Length should not be more than 9 characters.')
        ret_val = False

    if 'UMGC' in passwd or 'umgc' in passwd:
        print('The password cannot have UMGC anywhere in phrase.')
        ret_val = False

    if not '#' in passwd or '#' in passwd[0] or '#' in passwd[-1]:
        print('The password must have # somewhere beyond the first or last place.')
        ret_val = False

    if ret_val == True:
        print("Password meets parameters.")

passwd_check(passwd)
