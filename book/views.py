from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookForm
from .models import Book


def index(request):
    books = Book.objects.all()

    return render(request, 'book/index.html', {
        'books': books
    })


def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'book/detail.html', {
        'book': book
    })


def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('book:index')
    else:
        form = BookForm()

    return render(request, 'book/add.html', {
        'form': form
    })


def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()

            return redirect('book:index')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'book/edit.html', {
        'form': form
    })


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()

    return redirect('book:index')