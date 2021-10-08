from django.urls import path
from . import views

urlpatterns=[
    path('',views.getNotes),
    path('notes/',views.getNotes),
    path('notes/create/',views.creatNote),
   
    path('notes/update/<str:pk>',views.updateNote),

    path('notes/<str:pk>/',views.getNote),
    path('notes/delete/<str:pk>',views.deleteNote),

    
]