from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('tab',views.table, name='tab'),
    path('delete/<int:pk>',views.delete,name='delete'),
    #path('edit', views.edit, name='edit'),
    path('update/', views.update, name='update'),
    path('login',views.login, name='login'),
    path('loginn',views.loginn, name='loginn'),





]
