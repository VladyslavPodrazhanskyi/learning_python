class Rect():
    recs = []
    def __init__(self, w, l):
        self.w = w
        self.l = l
        Rect.recs.append((self.w, self.l))




rec1 = Rect(1, 2)
rec2 = Rect(1, 4)
rec3 = Rect(5, 4)
rec4 = Rect(7, 2)
rec5 = Rect(3, 18)


print(rec1.recs)

del(rec3)

print(rec1.recs)