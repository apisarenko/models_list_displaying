from django.shortcuts import render
from .models import Book
import datetime


def books_view(request, date=None):
    template = 'books/books_list.html'
    if date == None:
        books = Book.objects.all()
        context = {'books': books}
    else:
        date_books = datetime.datetime.date(datetime.datetime.strptime(date, "%Y-%m-%d"))
        books = Book.objects.filter(pub_date=date_books)
        list_next = Book.objects.all().order_by('pub_date').filter(pub_date__gt=date_books)
        if len(list_next) == 0:
            next_page = ''
        else:
            next_page = str(list_next[0].pub_date)
        list_page = Book.objects.all().order_by('pub_date').filter(pub_date__lt=date_books)
        if len(list_page) == 0:
            prev_page = ''
        else:
            prev_page = str(list_page[(len(list_page)) - 1].pub_date)

        context = {'books': books,
                   'prev_page': prev_page,
                   'next_page': next_page
                   }

    return render(request, template, context)
