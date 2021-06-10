class Page:
    __quantity = 0

    def __init__(self, number):
        self.number = number
        Page.__quantity += 1

    @classmethod
    def page_count(cls):
        return cls.__quantity

    def add_chapter(self, chapter):
        setattr(self, 'chapter', chapter)

p1 = Page(1)
p2 = Page(2)
p3 = Page(3)
p4 = Page(4)

print(p1.page_count())

print(Page.page_count())

p4.add_chapter(32)
print(p4.chapter)
p4.chapter = 64
print(p4.chapter)
p4.add_chapter(32)
print(p4.chapter)