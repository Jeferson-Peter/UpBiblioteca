from django.urls import path
from .views import cadastrar_book, listar_books, editar_book, remover_book, verify_status_book, cadastrar_loan
urlpatterns = [
    path('cadastrar_book', cadastrar_book, name='cadastrar_book'),
    path('listar_books', listar_books, name='listar_books'),
    path('editar_book/<int:book_id>', editar_book, name='editar_book'),
    path('remover_book/<int:book_id>', remover_book, name='remover_book'),
    path('book/<int:book_id>/', verify_status_book, name='verify_status_book'),
    path('book/<int:book_id>/loan/', cadastrar_loan, name='cadastrar_loan')
]