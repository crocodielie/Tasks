# TODO Найдите количество книг, которое можно разместить на дискете

space = 1.44    # Информационный объем дискеты в Мб
num_pages = 100    # Количество страниц в книге
num_lines = 50    # Число строк на странице
num_char = 25    # Количество символов в строке
weight_char = 4    # Вес одного символа

num_char_per_page = num_char * num_lines     # Количество символов на странице
num_char_in_book = num_pages * num_char_per_page    # количество символов в книге
book_weight = num_char_in_book * weight_char    # вес книги в байтах
book_weight_Mb = ( book_weight / 1024 ) / 1024      # вес книги в Мб
num_books_on_disk = space // book_weight_Mb

print("Количество книг, помещающихся на дискету:", int(num_books_on_disk))
