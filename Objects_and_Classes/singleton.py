class SingleTon:
    __instance = None

    def __new__(cls):
        if cls.__instance:
            print('Instance already exists')
            return cls.__instance
        print('Create singleton')
        return super(SingleTon, cls).__new__(cls)

    def __init__(self):
        type(self).__instance = self

single1 = SingleTon()
single2 = SingleTon()

print(single1 is single2)