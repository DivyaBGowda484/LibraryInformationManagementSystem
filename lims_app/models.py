from django.db import models
from django.utils import timezone

# Create your models here.

class Reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id = models.CharField(max_length=200)
    reader_name = models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_address = models.TextField()
    active = models.BooleanField(default=True)

class Book(models.Model):
    def __str__(self):
        return self.title
    
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    description = models.TextField(blank=True)
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_available(self):
        return self.available_copies > 0

class BorrowedBook(models.Model):
    def __str__(self):
        return f"{self.reader.reader_name} - {self.book.title}"
    
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    
    def is_overdue(self):
        return not self.is_returned and timezone.now() > self.due_date
    
    def days_overdue(self):
        if self.is_overdue():
            return (timezone.now() - self.due_date).days
        return 0