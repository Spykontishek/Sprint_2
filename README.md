1)test_add_new_book_add_books_with_different_limit_negative_values
Проверяем названием добавляемой книги негативные ГЗ по количеству символов(2 книги)
2)test_add_new_book_add_books_with_different_limit_positive_values
Проверяем названием добавляемой книги позитивные ГЗ по количеству символов(2 книги)
3)test_set_book_genre_successfully_added
Установка 1-ой добавленной книге определенного жанра
4)test_get_book_genre_use_name_in_books_genre
Добавляем книгу, устанавливаем ей жанр и проверяем, что метод вернул по названию книги именно этот жанр
5)test_get_books_with_specific_genre_use_setting_genre
Добавляем 2 книги, устанавливаем им 1 жанр и проверяем, что метод вернет по названию этого жанра обе книги, которые к нему принадлежит
6)test_get_books_genre_add_one_book
Добавляем книгу, устанавливаем ей жанр и проверяем, что метод вернул текущий словарь из books_genre в котором будет находиться эта книга
7)test_get_books_for_children_add_book_with_raiting_and_without_raiting_added_without_raiting
Добавляем 2 книги, 1-ой устанавливаем рейтинг подходящий для детей, другой - неподходящий, проверка, что метод вернет только книгу, подходящую детям
8)test_add_book_in_favorites_add_one_book
Добавляем книгу в books_genre и затем добавляем ее в избранные книги, проверяем, что метод вернет книгу находящуюсь в избранных книгах
9)обавляем книгу в books_genre и затем добавляем ее в избранные книги, удаляем ее из избранных, проверяем, что книги больше нет в избранных
10)test_get_list_of_favorites_books_add_one_book_in_favorite_getting_one_book
Добавляем 2 книги в books_genre и затем добавляем их в избранные книги, проверяем, что метод вернет обе книги, которые находятся в избранном
