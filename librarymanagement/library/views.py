from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.core.mail import send_mail
from librarymanagement.settings import EMAIL_HOST_USER
from django.shortcuts import render, redirect, get_object_or_404



def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'library/index.html')



def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'library/adminclick.html')



def adminsignup_view(request):
    form=forms.AdminSigupForm()
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'library/adminsignup.html',{'form':form})








def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'library/adminafterlogin.html')
    else:
        return render(request,'library/studentafterlogin.html')


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def addbook_view(request):
    #now it is empty book form for sending to html
    form=forms.BookForm()
    if request.method=='POST':
        #now this form have data from html
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'library/bookadded.html')
    return render(request,'library/addbook.html',{'form':form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def viewbook_view(request):
    books = models.Book.objects.all()
    return render(request, 'library/viewbook.html', {'books': books})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def edit_book_view(request, book_id):
    book = get_object_or_404(models.Book, id=book_id)
    form = forms.BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('view_book')
    return render(request, 'library/editbook.html', {'form': form})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_book_view(request, book_id):
    book = get_object_or_404(models.Book, id=book_id)
    book.delete()
    return redirect('view_book')

def aboutus_view(request):
    return render(request,'library/aboutus.html')



#@login_required(login_url='adminlogin')
#@user_passes_test(is_admin)
##add delete book

##add deleted books?


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)


def aboutus_view(request):
    return render(request,'library/aboutus.html')

