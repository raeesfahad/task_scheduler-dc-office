
from django.urls import path, include
from .views import *

urlpatterns = [
    path( "", index, name="home"),
    path( "login", login, name="login"),
     path( "logout", logout, name="logout"),
    path( "completed", completed, name="completed"),
    path( "urgent", urgent, name="urgent"),
    path('overdue', overdue, name="overdue"),
    path('search', partial_search, name="search"),
    path('update/<int:pk>/', complete_task, name="complete"),
    path('delete/<int:pk>/', delete_task, name="delete")
] 