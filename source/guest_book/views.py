from django.shortcuts import render
from guest_book.models import Page


# Create your views here.


def index_view(request):
    pages = Page.objects.filter(status="active").order_by('-created_at')
    context = {
        'pages': pages
    }
    return render(request, 'index.html', context)
