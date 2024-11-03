# TODO Найдите количество книг, которое можно разместить на дискете

symbol_size = 4
symbols_in_string = 25
number_of_string_on_page = 50
number_of_pages = 100
general_size = 1.44

size_of_all_symbols = (symbol_size * symbols_in_string * number_of_string_on_page * number_of_pages) / 1024 / 1024
number_of_books = int(general_size // size_of_all_symbols)

print("Количество книг, помещающихся на дискету:", number_of_books)
