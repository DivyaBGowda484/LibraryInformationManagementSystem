from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import admin, messages
from django.utils import timezone
from datetime import timedelta
from .models import *

def home(request):
    return render(request, 'home.html', context={"current_tab": "home"})

def readers(request):
    if request.method=="GET":
        readers = Reader.objects.all()
        return render(request, 'readers.html',
                      context={"current_tab": "readers",
                              "readers": readers}
                      )
    else:
        query = request.POST['query']
        readers = Reader.objects.raw("select * from lims_app_reader where reader_name like '%"+query+"%'")
    return render(request, 'readers.html',
                      context={"current_tab": "readers",
                              "readers": readers, "query": query}
                      )

def books(request):
    readers = Reader.objects.filter(active=True)
    if request.method == "GET":
        books = Book.objects.all()
        return render(request, 'books.html',
                      context={"current_tab": "books",
                              "books": books,
                              "readers": readers}
                      )
    else:
        query = request.POST['query']
        books = Book.objects.filter(title__icontains=query)
        return render(request, 'books.html',
                      context={"current_tab": "books",
                              "books": books, 
                              "readers": readers,
                              "query": query}
                      )

def my_bag(request):
    readers = Reader.objects.filter(active=True)
    if request.method == "GET":
        # For now, showing all borrowed books that are not returned
        borrowed_books = BorrowedBook.objects.filter(is_returned=False)
        return render(request, 'my_bag.html',
                      context={"current_tab": "my_bag",
                              "borrowed_books": borrowed_books,
                              "readers": readers}
                      )
    else:
        # Handle reader selection to show specific reader's bag
        reader_id = request.POST.get('reader_id')
        if reader_id:
            borrowed_books = BorrowedBook.objects.filter(reader_id=reader_id, is_returned=False)
        else:
            borrowed_books = BorrowedBook.objects.filter(is_returned=False)
        
        readers = Reader.objects.filter(active=True)
        return render(request, 'my_bag.html',
                      context={"current_tab": "my_bag",
                              "borrowed_books": borrowed_books,
                              "readers": readers,
                              "selected_reader": reader_id}
                      )

def returns(request):
    readers = Reader.objects.filter(active=True)
    if request.method == "GET":
        # Show all books that can be returned (borrowed but not returned)
        borrowed_books = BorrowedBook.objects.filter(is_returned=False)
        return render(request, 'returns.html',
                      context={"current_tab": "returns",
                              "borrowed_books": borrowed_books,
                              "readers": readers}
                      )
    else:
        # Handle reader selection to show specific reader's returns
        reader_id = request.POST.get('reader_id')
        if reader_id:
            borrowed_books = BorrowedBook.objects.filter(reader_id=reader_id, is_returned=False)
        else:
            borrowed_books = BorrowedBook.objects.filter(is_returned=False)
        
        readers = Reader.objects.filter(active=True)
        return render(request, 'returns.html',
                      context={"current_tab": "returns",
                              "borrowed_books": borrowed_books,
                              "readers": readers,
                              "selected_reader": reader_id}
                      )

def borrow_book(request):
    if request.method == 'POST':
        reader_id = request.POST.get('reader_id')
        book_id = request.POST.get('book_id')
        
        reader = get_object_or_404(Reader, id=reader_id)
        book = get_object_or_404(Book, id=book_id)
        
        if book.is_available():
            # Create borrowed book record
            due_date = timezone.now() + timedelta(days=14)  # 2 weeks borrowing period
            borrowed_book = BorrowedBook(
                reader=reader,
                book=book,
                due_date=due_date
            )
            borrowed_book.save()
            
            # Update available copies
            book.available_copies -= 1
            book.save()
            
            messages.success(request, f'Book "{book.title}" has been borrowed successfully!')
        else:
            messages.error(request, f'Book "{book.title}" is not available.')
    
    return redirect('/books')

def return_book(request, borrowed_book_id):
    borrowed_book = get_object_or_404(BorrowedBook, id=borrowed_book_id)
    
    if not borrowed_book.is_returned:
        # Mark book as returned
        borrowed_book.is_returned = True
        borrowed_book.returned_date = timezone.now()
        borrowed_book.save()
        
        # Update available copies
        book = borrowed_book.book
        book.available_copies += 1
        book.save()
        
        messages.success(request, f'Book "{book.title}" has been returned successfully!')
    else:
        messages.error(request, 'This book has already been returned.')
    
    return redirect('/returns')

def shopping(request):
    return HttpResponse("Welcome to the shopping page!")

def save_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        return render(request, 'welcome.html', {'student_name': student_name})
    return HttpResponse("Invalid Request Method")

def save_reader(request):
    reader_item = Reader(reference_id=request.POST['reader_ref_id'],
                         reader_name=request.POST['reader_name'],
                         reader_contact=request.POST['reader_contact'],
                         reader_address=request.POST['address'],
                         active=True
                         )
    reader_item.save()
    return redirect('/readers')

def save_book(request):
    if request.method == 'POST':
        book_item = Book(
            isbn=request.POST['isbn'],
            title=request.POST['title'],
            author=request.POST['author'],
            genre=request.POST['genre'],
            publication_year=request.POST['publication_year'],
            description=request.POST.get('description', ''),
            total_copies=int(request.POST['total_copies']),
            available_copies=int(request.POST['total_copies'])
        )
        book_item.save()
        messages.success(request, 'Book has been added successfully!')
    return redirect('/books')