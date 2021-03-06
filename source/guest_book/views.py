from django.shortcuts import render, redirect

from guest_book.forms import PageForm
from guest_book.models import Page


# Create your views here.


def index_view(request):
    pages = Page.objects.filter(status="active").order_by('-created_at')
    context = {
        'pages': pages
    }
    return render(request, 'index.html', context)


def form(args):
    pass


def page_create_view(request):
    if request.method == 'GET':
        page = PageForm()
        return render(request, 'page_create.html', context={'form': page})
    elif request.method == 'POST':
        page = PageForm(data=request.POST)
        if page.is_valid():
            page = Page(
                author=page.cleaned_data.get('author'),
                email=page.cleaned_data.get('email'),
                note_text=page.cleaned_data.get('note_text'),
            )
            page.save()
        else:
            return render(request, 'page_create.html', context={'form': page})
        return redirect('index')

