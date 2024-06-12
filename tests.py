import pytest
from main import BooksCollector


@pytest.mark.parametrize('name', ['', 'B' * 41, 'B' * 40, 'B'])
def test_add_new_book_add_books_with_different_limit_values(name):
    collector = BooksCollector()
    collector.add_new_book(name)
    assert 'B' * 41, '' not in collector.books_genre
    assert 'B', 'B' * 40 in collector.books_genre

def test_set_book_genre_successfully_added():
    collector = BooksCollector()
    collector.add_new_book('Book_1')
    collector.set_book_genre('Book_1', 'Фантастика')
    assert collector.books_genre['Book_1'] == 'Фантастика'

def test_get_book_genre_use_name_in_books_genre():
    collector = BooksCollector()
    collector.add_new_book('Book_1')
    collector.set_book_genre('Book_1', 'Фантастика')
    assert collector.get_book_genre('Book_1') == 'Фантастика'

def test_get_books_with_specific_genre_use_setting_genre_and_search_books_by_this_value():
    collector = BooksCollector()
    collector.add_new_book('Book_1')
    collector.add_new_book('Book_2')
    collector.set_book_genre('Book_1', 'Фантастика')
    collector.set_book_genre('Book_2', 'Фантастика')
    assert collector.get_books_with_specific_genre('Фантастика') == ['Book_1', 'Book_2']

def test_get_books_genre_add_one_book():
    collector = BooksCollector()
    collector.add_new_book('Book_1')
    collector.set_book_genre('Book_1', 'Фантастика')
    assert collector.get_books_genre() == {'Book_1': 'Фантастика'}

def test_get_books_for_children_add_book_with_raiting_and_without_raiting_added_without_raiting():
    collector = BooksCollector()
    collector.add_new_book('Book_1')
    collector.add_new_book('Book_2')
    collector.set_book_genre('Book_1', 'Фантастика')
    collector.set_book_genre('Book_2', 'Ужасы')
    assert collector.get_books_for_children() == ['Book_1']

def test_add_book_in_favorites_add_one_book():
    collector = BooksCollector()
    collector.add_new_book('Book_1')
    collector.add_book_in_favorites('Book_1')
    assert 'Book_1' in collector.get_list_of_favorites_books()

def test_delete_book_from_favorites_remove_one_book():
    collector = BooksCollector()
    collector.add_new_book('Book_1')
    collector.add_book_in_favorites('Book_1')
    collector.delete_book_from_favorites('Book_1')
    assert 'Book_1' not in collector.get_list_of_favorites_books()

def test_get_list_of_favorites_books_add_two_book_in_favorite_getting_two_book():
    collector = BooksCollector()
    collector.add_new_book('Book_1')
    collector.add_new_book('Book_2')
    collector.add_book_in_favorites('Book_1')
    collector.add_book_in_favorites('Book_2')
    assert collector.get_list_of_favorites_books() == ['Book_1', 'Book_2']

