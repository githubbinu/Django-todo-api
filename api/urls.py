from django.urls import path
from . import views

urlpatterns=[
    path('',views.getNotes),
    path('notes/',views.getNotes),
    path('notes/create/',views.creatNote),
     path('notes/api/create/',views.creatNote),
    path('notes/<str:pk>/update/',views.updateNote),

    path('notes/<str:pk>/',views.getNote),
    path('notes/delete/<str:pk>',views.deleteNote),

    
]