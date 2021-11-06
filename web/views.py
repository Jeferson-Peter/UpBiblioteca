from django.shortcuts import render, redirect
from .forms import book_form
from .models import Book, BookLoan
# Create your views here.

def cadastrar_book(request):
    if request.method == 'POST':
        form_book = book_form.BookForm(request.POST, request.FILES)
        if form_book.is_valid():
            book_title = request.POST.get('title')
            book_already_exists = Book.objects.filter(title = book_title)
            if not book_already_exists:
                form_book.save()
            return redirect('listar_books')
    else:
        form_book = book_form.BookForm()
    return render(request, 'form_book.html', {'form_book': form_book})

def listar_books(request):
    books = Book.objects.all()
    return render(request, 'lista_books.html', {'books': books})

def editar_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form_book = book_form.BookForm(request.POST or None,request.FILES, instance=book)
        if form_book.is_valid():
            form_book.save()
            return redirect('listar_books')
    else:
        form_book = book_form.BookForm(instance=book)
    return render(request, 'form_book.html', {'form_book': form_book})

def remover_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('listar_books')

def verify_status_book(request, book_id):
    book_loan = BookLoan.objects.filter(book_id=book_id)
    if not book_loan:
        return redirect('listar_books')
    elif book_loan:
        bookLoan = BookLoan.objects.get(book_id=book_id)
        book = Book.objects.get(id=book_id)
        author = book.author
        book_id = book.id
        return render(request, 'book_loan.html', {'bookLoan':bookLoan, 'author':author, 'book_id':book_id})

def cadastrar_loan(request, book_id):
    print(book_id)
    if request.method == 'POST':
        print(f"book_id: {book_id}")
        book = Book.objects.get(id=book_id)
        user = request.POST.get('user')
        borrowed = request.POST.get('borrowed')
        returned = request.POST.get('returned')
        print(borrowed, returned)
        if user == None or user == "":
            if borrowed == None or borrowed == "":
                if returned == None or returned == "":
                    return redirect('listar_books')
            return redirect('listar_books')

        book_loan = BookLoan(book_id=Book(id=book.id),
                             borrowed=borrowed,
                             returned=returned,
                             user=user)
        book_loan.save()
        return redirect('listar_books')
    else:
        form_book_loan = book_form.BookForm()
    return render(request, 'book_loan.html', {'form_book_loan': form_book_loan})