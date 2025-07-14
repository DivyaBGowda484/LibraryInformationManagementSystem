from django.contrib import admin
from django.utils import timezone
from datetime import timedelta
from django import forms
from .models import *

# Register your models here.

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ['reader_name', 'reference_id', 'reader_contact', 'active']
    list_filter = ['active']
    search_fields = ['reader_name', 'reference_id', 'reader_contact']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'genre', 'publication_year', 'available_copies', 'total_copies']
    list_filter = ['genre', 'publication_year']
    search_fields = ['title', 'author', 'isbn']
    readonly_fields = ['created_at']

class BorrowedBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Only show active readers
        self.fields['reader'].queryset = Reader.objects.filter(active=True)
        
        # For new records, only show available books
        if not self.instance.pk:
            self.fields['book'].queryset = Book.objects.filter(available_copies__gt=0)
            # Set default due date to 14 days from now
            self.fields['due_date'].initial = timezone.now() + timedelta(days=14)
            # Remove borrow_date from fields for new records since it's auto_now_add
            if 'borrow_date' in self.fields:
                del self.fields['borrow_date']
        else:
            # For existing records, show all books
            self.fields['book'].queryset = Book.objects.all()
    
    def clean_book(self):
        book = self.cleaned_data.get('book')
        if book and not self.instance.pk:  # Only check for new records
            if not book.is_available():
                raise forms.ValidationError(f"Book '{book.title}' is not available for borrowing.")
        return book
    
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        
        # For new records, compare with current time
        if not self.instance.pk:
            if due_date and due_date <= timezone.now():
                raise forms.ValidationError("Due date must be in the future.")
        else:
            # For existing records, compare with borrow_date
            if due_date and due_date <= self.instance.borrow_date:
                raise forms.ValidationError("Due date must be after borrow date.")
        
        return due_date

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    form = BorrowedBookForm
    list_display = ['reader', 'book', 'borrow_date', 'due_date', 'returned_date', 'is_returned', 'get_overdue_status', 'get_days_overdue']
    list_filter = ['is_returned', 'borrow_date', 'due_date']
    search_fields = ['reader__reader_name', 'book__title', 'book__author']
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing existing record
            return ['borrow_date', 'get_overdue_status', 'get_days_overdue']
        else:  # Adding new record
            return []
    
    def get_fieldsets(self, request, obj=None):
        if obj:  # Editing existing record
            return (
                ('Borrowing Information', {
                    'fields': ('reader', 'book', 'borrow_date', 'due_date'),
                    'description': 'Borrowing details for this transaction.'
                }),
                ('Status Information', {
                    'fields': ('get_overdue_status', 'get_days_overdue'),
                    'classes': ('collapse',),
                    'description': 'Current status of this borrowed book.'
                }),
                ('Return Information', {
                    'fields': ('is_returned', 'returned_date'),
                    'description': 'Mark as returned when book is returned.'
                }),
            )
        else:  # Adding new record
            return (
                ('Borrowing Information', {
                    'fields': ('reader', 'book', 'due_date'),
                    'description': 'Select the reader and book. Due date defaults to 14 days from today. Borrow date will be set automatically.'
                }),
                ('Return Information', {
                    'fields': ('is_returned', 'returned_date'),
                    'description': 'Leave these fields as default for new borrowings.'
                }),
            )
    
    def get_overdue_status(self, obj):
        return obj.is_overdue()
    get_overdue_status.boolean = True
    get_overdue_status.short_description = 'Overdue'
    
    def get_days_overdue(self, obj):
        if obj.is_overdue():
            return f"{obj.days_overdue()} days"
        return "Not overdue"
    get_days_overdue.short_description = 'Days Overdue'
    
    actions = ['mark_as_returned', 'mark_as_not_returned']
    
    def save_model(self, request, obj, form, change):
        # If this is a new borrowed book (not an update)
        if not change:
            # Update available copies for new borrowing
            if obj.book and obj.book.available_copies > 0:
                obj.book.available_copies -= 1
                obj.book.save()
        
        # If marking as returned and wasn't returned before
        if change:
            try:
                old_obj = BorrowedBook.objects.get(pk=obj.pk)
                if obj.is_returned and not old_obj.is_returned:
                    if not obj.returned_date:
                        obj.returned_date = timezone.now()
                    # Update available copies
                    obj.book.available_copies += 1
                    obj.book.save()
                
                # If marking as not returned and was returned before
                elif not obj.is_returned and old_obj.is_returned:
                    obj.returned_date = None
                    # Update available copies
                    if obj.book.available_copies > 0:
                        obj.book.available_copies -= 1
                        obj.book.save()
            except BorrowedBook.DoesNotExist:
                pass  # Handle case where object doesn't exist yet
        
        super().save_model(request, obj, form, change)
    
    def mark_as_returned(self, request, queryset):
        updated = 0
        for borrowed_book in queryset:
            if not borrowed_book.is_returned:
                borrowed_book.is_returned = True
                borrowed_book.returned_date = timezone.now()
                borrowed_book.save()
                
                # Update available copies
                book = borrowed_book.book
                book.available_copies += 1
                book.save()
                
                updated += 1
        
        self.message_user(request, f'{updated} books marked as returned.')
    mark_as_returned.short_description = 'Mark selected books as returned'
    
    def mark_as_not_returned(self, request, queryset):
        updated = 0
        for borrowed_book in queryset:
            if borrowed_book.is_returned:
                borrowed_book.is_returned = False
                borrowed_book.returned_date = None
                borrowed_book.save()
                
                # Update available copies
                book = borrowed_book.book
                book.available_copies -= 1
                book.save()
                
                updated += 1
        
        self.message_user(request, f'{updated} books marked as not returned.')
    mark_as_not_returned.short_description = 'Mark selected books as not returned'
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        # Customize help text and labels
        if not obj:  # Adding new record
            if 'reader' in form.base_fields:
                form.base_fields['reader'].help_text = "Select the reader who is borrowing the book."
            if 'book' in form.base_fields:
                form.base_fields['book'].help_text = "Select an available book to borrow."
            if 'due_date' in form.base_fields:
                form.base_fields['due_date'].help_text = "Due date defaults to 14 days from today. Borrow date will be set automatically."
            if 'is_returned' in form.base_fields:
                form.base_fields['is_returned'].help_text = "Leave unchecked for new borrowings."
            if 'returned_date' in form.base_fields:
                form.base_fields['returned_date'].help_text = "Leave blank for new borrowings."
        else:  # Editing existing record
            if 'borrow_date' in form.base_fields:
                form.base_fields['borrow_date'].help_text = "Automatically set when the book was borrowed."
            if 'returned_date' in form.base_fields:
                form.base_fields['returned_date'].help_text = "Will be set automatically when marked as returned."
        
        return form