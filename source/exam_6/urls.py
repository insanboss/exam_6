"""exam_6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from guest_book.views import (
    index_view,
    page_create_view,
    page_update_view,
    page_delete_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('page/add/', page_create_view, name='page_add'),
    path('page/<int:pk>/update/', page_update_view, name='page_update'),
    path('page/<int:pk>/delete/', page_delete_view, name='page_delete'),
]
