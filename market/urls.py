from django.urls import path
from . import views

urlpatterns = [
    path('',views.getBookslist, name='market'),
    path('delete.html/<str:pk>',views.deleteBook,name='delete')
  
]
