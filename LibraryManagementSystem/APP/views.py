from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.cache import cache_control
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def backend(request):
    students = Student.objects.all()
    
    context = {}
    context['student'] = students
    
    return render(request, 'backend.html', context)


@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def entry(request):
    context = {}
    students = Student.objects.all()
    context['student'] = students
    
    entries = Entry.objects.all()
    context['entry'] = entries
    return render(request, 'entry.html', context)

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def delete_student(request, request_id):
    student = Student.objects.get(id=request_id)
    student.delete()
    messages.success(request, 'Student deleted successfully')
    return HttpResponseRedirect('/backend')


def edit_student(request, requested_id):
    student = Student.objects.get(id=requested_id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.prn = request.POST['prn']
        student.branch = request.POST['branch']
        student.year = request.POST['year']

        student.save()
        messages.success(request, 'Information updated successfully.')
        return HttpResponseRedirect('/backend')

    return render(request, 'edit.html', {'student':student})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        prn = request.POST['prn']
        branch = request.POST['branch']
        year = request.POST['year']

        student = Student(name=name, prn=prn, branch=branch, year=year)
        student.save()
        messages.success(request, 'Student added successfully.')
        return HttpResponseRedirect('/backend')


def add_entry(request):
    if request.method == 'POST':
        name = request.POST['name']
        book = request.POST['book']
        
        student = Student.objects.get(name=name)
        entry = Entry(Student=student, Book_issued=book)
        entry.save()
        messages.success(request, 'Entry is done successfully.')
        return HttpResponseRedirect('/backend')

def del_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    entry.delete()
    messages.success(request, 'Entry deleted successfully')
    return HttpResponseRedirect('/backend')
