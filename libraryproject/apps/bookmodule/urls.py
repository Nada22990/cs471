"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views



urlpatterns = [
    
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),

    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.formatting, name="books.formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),


    path('search', views.search),
    path('simple/query', views.simple_query),
    path('complex/query', views.complex_query),
    path('lab8/task1', views.task1),
    path('lab8/task2', views.task2),
    path('lab8/task3', views.task3),
    path('lab8/task4', views.task4),
    path('lab8/task5', views.task5),
    path('lab8/task7', views.task7),
    path('lab9/task22', views.task22),
    path('lab9/task33', views.task33),
    path('lab9/task44', views.task44),
    path('lab9/task55', views.task55),
    path('lab9_part1/listbooks', views.listbooks, name="list_books"),
    path('lab9_part1/addbook', views.addbook, name="add_book"),
    path('lab9_part1/editbook/<int:id>', views.editbook, name="edit_book"),
    path('lab9_part1/deletbook/<int:id>', views.deletbook, name="delet_book"),

     path('lab9_part2/listbooks2', views.listbooks2, name="list_books2"),
    path('lab9_part2/addbook2', views.addbook2, name="add_book2"),
    path('lab9_part2/editbook2/<int:id>', views.editbook2, name="edit_book2"),
    path('lab9_part2/deletbook2/<int:id>', views.deletbook2, name="delet_book2"),

    
    path('simple/query1', views.simp),
    path('complex/query1', views.comp),

##############################################################Task1

    path('students/list/', views.list_students, name="list_students"),
    path('students/add/', views.addstudent, name="add_student"),
    path('students/edit/<int:id>/', views.editstudent, name="edit_student"),
    path('students/delete/<int:id>/', views.deletestudent, name="delete_student"),


##############################################################Task2

    path('students/list2/', views.list_students2, name="list_students2"),
    path('students/add2/', views.addstudent2, name="add_student2"),
    path('students/edit2/<int:id>/', views.editstudent2, name="edit_student2"),
    path('students/delete2/<int:id>/', views.deletestudent2, name="delete_student2"),

 ###########################################################################################Task3
 
    path('profiles/list', views.list_profiles, name='list_profiles'),
    path('profiles/add/', views.add_profile, name='add_profile'),
    path('profiles/edit/<int:id>/', views.edit_profile, name='edit_profile'),
    path('profiles/delete/<int:id>/', views.delete_profile, name='delete_profile'),

    
]


