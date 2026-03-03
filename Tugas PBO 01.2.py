class Book:
    def __init__(self, tittle, author, isbn):
        self.tittle = tittle
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print("\nBuku berhasil dipinjam.")
        else:
            print("\nBuku sudah dipinjam.")
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("\nBuku berhasil dikembalikan.")
        else:
            print("\nBuku sudah tersedia.")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
class staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

class BorrowTransaction:
    def __init__(self, book, member, staff, borrow_date):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = borrow_date
        self.returned = False
    def borrow_book(self):
        if not self.book.is_borrowed:
            self.book.borrow()
            self.member.borrowed_books.append(self.book)
            self.returned = False
        else:
            print("\nTransaksi gagal, buku sedang dipinjam.")
    def return_book(self):
        if not self.returned:
            self.book.return_book()
            if self.book in self.member.borrowed_books:
                self.member.borrowed_books.remove(self.book)
            self.returned = True
        else:
            print("\nBuku sudah dikembalikan sebelumnya.")

book1 = Book("Pemrograman python", "Andi", "B001")
member1 = Member("Zura", "M001")
staff1 = staff("Budi", "S001")

transaksi1 = BorrowTransaction(book1, member1, staff1, "04-03-2026")

transaksi1.borrow_book()
transaksi1.return_book()
