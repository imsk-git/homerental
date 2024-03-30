from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutPage, name='logout'),
    path('create/',views.create,name='create'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('register/',views.register, name='register'),
    path('detail/<int:id>/', views.detailView,name = 'details' ),
    path('book_now/<int:id>',views.book,name='book')
]