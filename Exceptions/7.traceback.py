import traceback

try:
    print(5 / 0)

except Exception as e:
    traceback.print_exc()
    print(type(e))
    print(str(e))
    print(e)


