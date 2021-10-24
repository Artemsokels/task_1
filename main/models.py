from pony.orm import *


db = Database()


class Author(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    surname = Required(str)
    age = Optional(int)
    email = Required(str, unique=True)
    login = Required(int)
    books = Set('Books')


class Books(db.Entity):
    id = PrimaryKey(int, auto=True)
    page_count = Required(int)
    name = Required(str)
    prise = Required(float)
    author = Required(Author)



db.generate_mapping()