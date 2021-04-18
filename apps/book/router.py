# coding: utf-8
from rest_framework import routers
from apps.book import views

# book_router = routers.SimpleRouter()
book_router = routers.DefaultRouter()

book_router.register(r"v20/book/publisher", views.PublisherModelViewSet)
book_router.register(r"v20/book/books", views.BookModelViewSet)
book_router.register(r"v22/book/books", views.BookBaseModelViewSet)

print(book_router.urls)