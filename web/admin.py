from django.contrib import admin
from .models import  Book, BookLoan
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author')
    search_fields = ('title', 'author', 'id')

@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'borrowed', 'returned', 'book_id')
    search_fields = ('id', 'user', 'borrowed', 'returned', 'book_id')
