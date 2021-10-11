from marshmallow import Schema, fields, EXCLUDE, INCLUDE


class Book:
    def __init__(self, title, author, pages, description=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description

    def __repr__(self):
        return f"Book title: {self.title}, author: {self.author}, pages: {self.pages}, description: {self.description}"

# book_obj = Book('The Seven Habits', 'Steven Covey', 825)
# print(book_obj)



class BookSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    pages = fields.Int(required=True)
    description = fields.Str()



book_schema = BookSchema(unknown=EXCLUDE)



incoming_book_data = {
    'title': 'Theoretical physics',
    'author': "Landau",
    'pages': '5',
    'ISBN': 23473297487
}


loaded_book_dict = book_schema.load(incoming_book_data)


book_obj = Book(**loaded_book_dict)
print(book_obj, type(book_obj))