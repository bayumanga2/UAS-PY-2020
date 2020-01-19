from core.baseapp import BaseApp
from data_model import book
from data_model.book import Book

class MainApp():
    def _init_(self):
        self.books = []
        self.inputBook = []
        self.ViewBook = []
        BaseApp.__init__(self)

class ViewBook(Book):
    def _init_(self):
        vBook = ViewBook(self,book)
        vBook.list_book()


if __name__ == "__main__":
    app = MainApp()
    app.run ()

