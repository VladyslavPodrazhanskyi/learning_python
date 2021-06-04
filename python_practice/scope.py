token = 'global'

def access_local():
    token = 'local'
    if 'token' in locals() and 'token' in globals():
        print("Yes, token is in both local and global scope")
        print("But value of the token is: ", token)


def access_global():
    if 'token'  in globals():
        print("value of the token is: ", token)


def access_enclosed():
    test = 1
    for test in range(5):
        token = f'enclosed'
        pass
    if 'token' in globals():
        print("Though token is in global scope")
        print("value of the token is: ", test)

access_enclosed()