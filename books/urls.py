from django.urls import path
from .views import *

urlpatterns = [
    # Other URL patterns
    path('books/', BooksScrapper, name='books_scrapper'),
]
