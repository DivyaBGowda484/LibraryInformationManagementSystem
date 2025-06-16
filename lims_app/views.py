from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import admin
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