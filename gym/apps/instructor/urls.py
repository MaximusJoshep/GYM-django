from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('form', views.register, name = "form"),
    path('create', views.create, name = "create"),
    path('edit/<id>', views.edit, name = "edit"),
    path('modify/<id>', views.modify, name = "modify"),
    path('delete/<id>', views.delete, name = "delete"),
    path('view/<id>', views.view, name = "view"),
   

]