# TODO Найдите количество книг, которое можно разместить на дискете
page = 100
line = 50
symbols = 25
bytes_ = 4
floppy = 1.44
volume_of_data = floppy * (1024 ** 2)
one_book_memory = page * line * symbols * bytes_
number_of_books = int(volume_of_data // one_book_memory)
print("Количество книг, помещающихся на дискету:", number_of_books)
