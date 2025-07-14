from django.urls import path
from .views import *

urlpatterns = [
    path('', home), 
    path('home', home),
    path('readers', readers),
    path('books', books),
    path('my_bag', my_bag),
    path('returns', returns),
    path('save', save_student),
    path('readers/add', save_reader),
    path('books/add', save_book),
    path('borrow_book', borrow_book),
    path('return_book/<int:borrowed_book_id>', return_book),
]
