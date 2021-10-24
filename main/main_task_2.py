import os.path
from fastapi import FastAPI, Body
import uvicorn
from models import db, Author, Books
from pony.orm import db_session, commit
from shema import Return_all_books

app = FastAPI()
DATABASE_FILENAME = 'author_and_books.sqlite'

@app.on_event('startup')
async def start_app():
    create_db = True
    if os.path.istfile(DATABASE_FILENAME):
        create_db = False
    db.bind(provider='sqlite', filename=DATABASE_FILENAME, create_db=create_db)
    db.generate_mapping(create_tables=create_db)

@app.get('/api/products')
async def return_all_books():
    with db_session:
        books = Book.select()
        all_books = []
        for i in books:
            all_books.append(books)
    if all_books == []:
        return 'Нет существующих книг'
    return all_books


if __name__ == '__main__':
    uvicorn.run('main:app', host='lacalhost', port=8000, reload=True)