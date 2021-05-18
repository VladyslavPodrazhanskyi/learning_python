try:
    if '1' != 1:
        raise 'Error'
    else:
        print('Error has not occurred')
except "Error":
    print("Error has occurred")
