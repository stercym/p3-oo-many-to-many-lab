class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    def contracts(self):
        """Return a list of contracts related to this book."""
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        """Return a list of authors related to this book through contracts."""
        return [c.author for c in self.contracts()]

    def __repr__(self):
        return f"Book(title='{self.title}')"


class Author:
    all = []

    def __init__(self, name: str):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    def contracts(self):
        """Return a list of contracts related to this author."""
        return [c for c in Contract.all if c.author == self]

    def books(self):
        """Return a list of books related to this author through contracts."""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract for this author and given book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total royalties earned from all contracts."""
        return sum(c.royalties for c in self.contracts())

    def __repr__(self):
        return f"Author(name='{self.name}')"


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author object")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be a Book object")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("royalties must be a number")
        if value < 0:
            raise Exception("royalties cannot be negative")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts signed on the given date."""
        return [c for c in cls.all if c.date == date]

    def __repr__(self):
        return (f"Contract(author={self.author.name}, book={self.book.title}, "
                f"date='{self.date}', royalties={self.royalties})")
