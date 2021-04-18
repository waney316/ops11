from django.urls import path, re_path

from apps.book import views

urlpatterns = [
    path('v1/book/publisher', views.PrintHello),
    path('v2/book/publisher', views.PublishView.as_view()),
    path('v3/book/publisher', views.PublisherApiView.as_view()),
    path('v3/book/publisher/<int:pk>', views.PublisherApiView.as_view()),

    # generic api view
    path('v4/book/publisher', views.PublisherListAPIView.as_view()),  # get: ListAPIView
    path('v8/book/publisher/<int:pk>', views.PublisherRetrieveAPIView.as_view()),  # get: sample data
    path('v5/book/publisher', views.PublisherCreateAPIView.as_view()),  # post: CreateAPIView
    path('v6/book/publisher/<int:pk>', views.PublisherDestroyAPIView.as_view()),  # delete: DestroyAPIView
    path('v7/book/publisher/<int:pk>', views.PublisherUpdateAPIView.as_view()),  # update: UpdateAPIView
    path('v10/book/publisher/<int:pk>', views.PublisherListCreateAPIView.as_view()),  # update: UpdateAPIView

]
